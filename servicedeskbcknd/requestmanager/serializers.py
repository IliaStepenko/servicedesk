from rest_framework import serializers
from .models import BusinessSystemDictionary, PriorityDictionary


class BusinessSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessSystemDictionary
        fields = ('name',)


class PriorityDictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = PriorityDictionary
        fields = ('name', 'ru_name')

