from django.shortcuts import render
from rest_framework import generics
from .serializers import BasicInformationSerializers
from .models import BasicInformation
from rest_framework import mixins
from .serializers import BasicInformationSerializers
from .models import BasicInformation


class BasicInformationList(generics.ListCreateAPIView):
    queryset = BasicInformation.objects.all()
    serializer_class = BasicInformationSerializers


class BasicInformationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BasicInformation.objects.all()
    serializer_class = BasicInformationSerializers

