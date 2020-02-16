from django.contrib import admin

# Register your models here.

from .models import BusinessSystemDictionary, SDRequest, PriorityDictionary


admin.site.register(BusinessSystemDictionary)
admin.site.register(PriorityDictionary)
admin.site.register(SDRequest)


