from django.test import TestCase
from .models import Image,Profile


# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(bio='Life is too short')
    def test_instances(self):
        self.assertTrue(isinstance(self.profile,Profile))
    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profles) > 0)   
    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profiel) == 0)
    def test_search_by_profile(self):
        profiles = Profile.search_profile('')
        self.assertTrue(len(profiles)>0)  

class ImageTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.profile = Profile(bio='Life is too short',image='',user='')
        self.proile.save_profile()


        self.image = Image(name='image test', image='my test',caption='a caption test', profile='', profile_det=self.profile)
        self.image.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def tearDown(self):
        self.image.delete_image()
        self.profile.delete_profile()


    def test_save_method(self):
        self.image.save_image()
        images  = Image.objects.all()
        self.assertTrue(len(images)>0)


    def test_get_all_images(self):
        images = Image.get_all_images()
        self.assertTrue(len(images)>0)

    def test_get_image_by_id(self):
        images= Image.get_image_by_id(self.image.id)
        self.assertTrue(len(images) == 1)

    def test_get_profile_pic(self):
        images = Image.get_profile_pic(profile.id)
        self.assertTrue(len(images)>0)

   

