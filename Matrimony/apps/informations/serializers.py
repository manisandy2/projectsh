from rest_framework import serializers
from .models import BasicInformation


class BasicInformationSerializers(serializers.ModelSerializer):
    class Meta:
        model = BasicInformation
        fields = "__all__"



