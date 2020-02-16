import random
import string

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class DepartmentDictionary(models.Model):
    name = models.CharField(max_length = 50, blank = True)
    ru_name = models.CharField('ru_name', max_length=50, blank=True)

class LocationDictionary(models.Model):
    name = models.CharField('name', max_length=50)
    ru_name = models.CharField('ru_name', max_length=50, blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.OneToOneField(LocationDictionary, null=True ,on_delete=models.SET_NULL)
    department = models.OneToOneField(DepartmentDictionary, null=True, on_delete=models.SET_NULL )
    birth_date = models.DateTimeField(null=True, blank=True)
    data_dir = models.CharField(max_length=50, blank = True, null=True)





@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created :
        Profile.objects.create(user=instance, data_dir=generate_folder_name())

@receiver(post_save, sender=User)
def create_auth_token(sender, instance, created, **kwargs):
    if created :
        Token.objects.create(user=instance)



@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



def generate_folder_name():
    string_length = 10
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))
