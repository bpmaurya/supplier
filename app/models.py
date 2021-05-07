from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_NULL
from django.utils.deconstruct import deconstructible
import os

@deconstructible
class GenerateProfileImagePath(object):
    def __init__(self):
        pass
    def __call__(self,instance,filename):
        ext = filename.split('.')[-1]
        path = f'media/account/{instance.user.id}/images'
        name = f'profile_image.{ext}'
        return os.path.join(path,name)

user_profile_image_path = GenerateProfileImagePath()


class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_profile_image_path,blank=True,null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user.username}\'s Profiles'

class Contact(models.Model):
    sno = models.AutoField(primary_key= True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=45)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return 'Message from '+ self.name + ' - '+self.email        

class Supplier(models.Model):
    pass