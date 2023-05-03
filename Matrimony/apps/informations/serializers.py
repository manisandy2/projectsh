from rest_framework import serializers
from .models import BasicInformation,Caste,SubCaste


class BasicInformationSerializers(serializers.ModelSerializer):
    class Meta:
        model = BasicInformation
        fields = "__all__"


class CasteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Caste
        fields = "__all__"


class SubCasteSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubCaste
        fields = "__all__"
