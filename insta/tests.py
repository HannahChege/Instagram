from django.test import TestCase
from .models import Image,Profile


# Create your tests here.
class ProfileTestClass(TestCase):
class ProfileTestClass(TestCase):
    """
    Test profile class and its functions
    """
    def setUp(self):

        self.user = User.objects.create(id =1,username='hannah')
        self.profile = Profile(dp='hannah.jpg', bio='Life is too short', contact="0711139310",user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_method(self):
        """
        Function to test that profile is being saved
        """
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        """
        Function to test that a profile can be deleted
        """
        self.profile.save_profile()
        

    def test_update_method(self):
        """
        Function to test that a profile's details can be updated
        """
        self.profile.save_profile()
        new_profile = Profile.objects.filter(bio='LIfe is too short').update(bio='You only live once')

    
    def test_get_profile_by_id(self):
        """
        Function to test if you can get a profile by its id
        """
        self.profile.save_profile()
        this_pro= self.profile.get_by_id(self.profile.user_id)
        profile = Profile.objects.get(user_id=self.profile.user_id)
        self.assertTrue(this_pro, profile)

class CommentTestClass(TestCase):
    #set up method
    def setUp(self):
        self.coments = Comment(description = 'comment')
    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.coments,Comment))
    #testing for savinng method
    def test_save_method(self):
        self.coments.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) > 0)
    #testng for deleting method
    def test_delete_method(self):
        self.coments.save_comment()
        self.coments.delete_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) == 1 )         
class ImageTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.image = Image(image = 'fashion')
    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def tearDown(self):
        self.image.delete_image()
        self.profile.delete_profile()


    def test_save_method(self):
        self.image.save_image()
        images  = Image.objects.all()
        self.assertTrue(len(images)>0)
    def test_delete_method(self):
        self.image.save_image()
        self.image.delete_image()
        image = Image.objects.all()
        self.assertTrue(len(image) > 0)
    def test_update_metod(self):
        self.image.save_image()
        self.image.update_caption()
        image = Image.objects.all()
        self.assertTrue(len(image) > 0)    

    def test_get_all_images(self):
        images = Image.get_all_images()
        self.assertTrue(len(images)>0)

    def test_get_image_by_id(self):
        images= Image.get_image_by_id(self.image.id)
        self.assertTrue(len(images) == 1)

    

