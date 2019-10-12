from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length =30)

    def __str__(self):
        return self.location

    @classmethod
    def get_location_id(cls,id):
        locate = Location.objects.get(pk=id)
        return locate


    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()

    def update_location(self, update):
        self.location = update
        self.save()

    class Meta:
        ordering = ['location']

class category(models.Model):
    cname = models.CharField(max_length =30)

    def __str__(self):
        return self.cname
        
    def save_category(self):
        self.save()
    
    def delete_category(self):
        self.delete()

    def update_category(self,update):
        self.cname = update
        self.save()

    @classmethod
    def get_category_id(cls,id):
        cats = category.objects.get(pk=id)
        return cats

class Image(models.Model):
    name = models.CharField(max_length =60)
    description = models.TextField()
    location = models.ForeignKey(Location,db_column='location')
    category = models.ForeignKey(category,db_column='cname')
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'articles/', )

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()

    def update_image(self,update):
        self.image = update
        self.save()

    @classmethod
    def displaying_images(cls):
        all_images = cls.objects.all()
        return all_images

    @classmethod
    def get_image_by_id(cls, id):
        images = cls.objects.filter(id = id)
        return images

    @classmethod
    def filter_by_location(cls, id):
        images = cls.objects.filter(location_id=id)
        return images

    @classmethod
    def search_image(cls,search_term):
        categories = Image.objects.filter(category__cname__contains=search_term)
        return categories

    @classmethod
    def filter_by_category(cls,category):
        category = cls.objects.filter(category=category)
        return category
    