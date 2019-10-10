from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length =30)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

    class Meta:
        ordering = ['location']

class category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length =60)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(category)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'articles/', )

    @classmethod
    def displaying_images(cls):
        all_images = cls.objects.all()
        return all_images

    @classmethod
    def get_image_by_id(cls,id):
        images = cls.objects.filter(id = id)
        return images

    @classmethod
    def filter_by_location(cls,location):
        locate = cls.objects.filter(location = location)
        return locate

    @classmethod
    def search_image(cls,category):
        categories = cls.objects.filter(category__icontains=search_term)
        return categories

    @classmethod
    def filter_by_category(cls,category):
        category = cls.objects.filter(category=category)
        return category
    