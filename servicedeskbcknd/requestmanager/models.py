from django.db import models

# Create your models here.



from usermanager.models import Profile, LocationDictionary



class BusinessSystemDictionary(models.Model):
    name = models.CharField('BSName', max_length=120)


class PriorityDictionary(models.Model):
    name = models.CharField('name', max_length=10)
    ru_name = models.CharField('ru_name', max_length=10,blank=True)

class RequestStatusDictionary(models.Model):
    name = models.CharField('name', max_length=10)
    ru_name = models.CharField('ru_name', max_length=10, blank=True)

class PositionDictionary(models.Model):
    name = models.CharField('name', max_length=10)
    ru_name = models.CharField('ru_name', max_length=10, blank=True)






class SDRequest(models.Model):
    status = models.OneToOneField(RequestStatusDictionary, related_name='status', null=True, on_delete=models.SET_NULL)
    customer = models.OneToOneField(Profile, related_name='customer', on_delete=models.CASCADE)
    recipient = models.OneToOneField(Profile, related_name='recipient', on_delete=models.CASCADE)
    position = models.OneToOneField(PositionDictionary, related_name='position', null=True, on_delete=models.SET_NULL)
    location = models.OneToOneField(LocationDictionary, related_name='location', null=True, on_delete=models.SET_NULL)
    priority = models.OneToOneField(PriorityDictionary, related_name='priority', null=True, on_delete=models.SET_NULL)
    bs_system = models.OneToOneField(BusinessSystemDictionary, related_name='bs_system', null=True, on_delete=models.SET_NULL)
    pc_info = models.CharField('pc_info', max_length=128, blank=True)
    theme = models.CharField('theme', max_length=128, blank=True)
    ip_adress = models.CharField('ip_adress', max_length=20, blank=True)
    create_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField('description',blank=True)


