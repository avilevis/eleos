from rest_framework import serializers
from .models import ZoomModel


class ZoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZoomModel
        fields = '__all__'
