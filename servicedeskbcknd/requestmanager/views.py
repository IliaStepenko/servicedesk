from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from servicedeskbcknd.requestmanager import serializers
from servicedeskbcknd.requestmanager.models import BusinessSystemDictionary, PriorityDictionary


class BusinessSystemViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = BusinessSystemDictionary.objects.all()
    serializer_class = serializers.BusinessSystemSerializer


class PriorityDictionaryViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = PriorityDictionary.objects.all()
    serializer_class = serializers.PriorityDictionarySerializer