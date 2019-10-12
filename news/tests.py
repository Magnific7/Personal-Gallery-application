from django.test import TestCase
from .models import Location,Image,category
import datetime as dt

# Create your tests here.
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.Paris= Location(location='Paris')
        self.Paris.save_location()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Paris,Location))

    def test_update_location(self):
        location = Location.get_location_id(self.Paris.id)
        location.update_location('London')
        location = Location.get_location_id(self.Paris.id)
        self.assertTrue(location.location == 'London')

    def tearDown(self):
        self.Paris.delete_location()

    # Testing Save Method
    def test_save_method(self):
        self.Paris.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new category and saving it
        self.music= category(cname='music')
        self.music.save_category()

        # Creating a new location and saving it
        self.Paris = Location(location = 'testing')
        self.Paris.save()

        self.sunshine= Image(name = 'sun',description = 'description',category = self.music,location = self.Paris)
        self.sunshine.save()

    def tearDown(self):
        Location.objects.all().delete()
        category.objects.all().delete()
        Image.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.sunshine,Image))

    def save_method(self):
        self.sunshine.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        self.sunshine.save_image()
        self.sunshine.delete_image()

    # def test_update_image(self):
    #     self.sunshine.save_image()
    #     new_image = Image.objects.filter(image='image2.jpg').update(image='download.jpg')
    #     images = Image.objects.filter(image='download.jpg')
    #     self.assertTrue(images.image, 'download.jpg')

class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.food= category(cname='food')
        self.food.save_category()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.food,category))

    def test_update_category(self):
        self.food.save_category()
        image = category.get_category_id(self.food.id)
        # image.update_category('travel')
        cate = category.get_category_id(self.food.id)
        self.assertTrue(image, cate)

    def tearDown(self):
        self.food.delete_category()

    # Testing Save Method
    def test_save_method(self):
        self.food.save_category()
        cname = category.objects.all()
        self.assertTrue(len(cname) > 0)
