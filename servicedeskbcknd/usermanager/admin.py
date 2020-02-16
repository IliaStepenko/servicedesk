from django.contrib import admin

# Register your models here.
from .models import Profile, DepartmentDictionary, LocationDictionary

admin.site.register(Profile)

admin.site.register(DepartmentDictionary)
admin.site.register(LocationDictionary)
