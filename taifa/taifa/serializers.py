from rest_framework import serializers
from .models import taifa


class taifaserials(serializers.ModelSerializer):
    class Meta:
        model = taifa
        fields = ['id', 'name', 'description']