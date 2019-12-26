from rest_framework import serializers
from .models import date


class DateSerializer(serializers.ModelSerializer):

    class Meta:
        model = date
        fields = '__all__'
