from django.shortcuts import render
from rest_framework import generics
from .serializers import BasicInformationSerializers
from .models import BasicInformation
from rest_framework import mixins
from .serializers import BasicInformationSerializers,CasteSerializers,SubCasteSerializers
from .models import BasicInformation,Caste,SubCaste


class BasicInformationList(generics.ListCreateAPIView):
    queryset = BasicInformation.objects.all()
    serializer_class = BasicInformationSerializers


class BasicInformationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BasicInformation.objects.all()
    serializer_class = BasicInformationSerializers


class CasteList(generics.ListCreateAPIView):
    queryset = Caste.objects.all()
    serializer_class = CasteSerializers


class CasteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Caste.objects.all()
    serializer_class = CasteSerializers


class SubCasteList(generics.ListCreateAPIView):
    queryset = SubCaste.objects.all()
    serializer_class = SubCasteSerializers


class SubCasteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubCaste.objects.all()
    serializer_class = SubCasteSerializers
