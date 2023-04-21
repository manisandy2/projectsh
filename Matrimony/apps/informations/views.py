from django.shortcuts import render
from rest_framework import generics
from .serializers import BasicInformationSerializers
from .models import Basic_Information


class BasicInformationList(generics.ListCreateAPIView):
    queryset = Basic_Information.objects.all()
    serializer_class = BasicInformationSerializers


class BasicInformationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Basic_Information.objects.all()
    serializer_class = BasicInformationSerializers
    