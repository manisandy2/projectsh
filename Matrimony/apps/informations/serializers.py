from rest_framework import serializers
from .models import Basic_Information


class BasicInformationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Basic_Information
        fields = "__all__"