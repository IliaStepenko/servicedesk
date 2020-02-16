from django.contrib.auth.models import User
from rest_framework import serializers
from . import models


class DepartmentDictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DepartmentDictionary
        fields = ('name',)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = ('location', 'department', 'birth_date', 'data_dir')

class RegistrationSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only' : True}
        }

    def save(self):
        user = User(
            email = self.validated_data['email'],
            username = self.validated_data['username']
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user