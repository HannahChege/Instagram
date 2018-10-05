from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# # Create your models here.
class Profile(models.Model):
    prof_image = models.ImageField(upload_to='insta/', blank=True)
    bio = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    def save_profile(self):
        self.save() 

    @classmethod
    def update_profile(cls,update):
        pass
    def delete_profile(self):
        self.delete()  
    @classmethod
    def search_by_profile(cls,name):
        profile = Profile.objects.filter(profile__insta_profile__icontains=search_term)
        return profile   

# class Image (models.Model):
#     image = models.ImageField(upload_to = 'insta/', default='No image')
#     image_name = models.CharField(max_length =500)
#     image_caption = HTMLField(blank=True)
#     # likes = models.ManyToManyField(likes)
#     # comment = models.ManyToManyField(comment)
#     profile = models.ForeignKey(User, on_delete=models.CASCADE)
#     pub_date = models.DateTimeField(auto_now_add=True, null=True) 
#     class Meta:
#         ordering = ('-pub_date',)
#     def save_image(self):
#         self.save() 
#     @classmethod
#     def update_caption(cls,update):
#         pass
#     def delete_image(self):
#         self.delete()    
#     def display_images(cls):
#         images=cls.objects.all()
#         return images  
# class Like(models.Model):
#     name = models.CharField(max_length =30)

#     def __str__(self):
#         return self.name
# class Comment(models.Model):
#     name = models.CharField(max_length =30)

#     def __str__(self):
#         return self.name
