from rest_framework import serializers
from .models import Absence



class AbsenceSerializer(serialisers.ModelSerialiser):
    class Meta:
        model = Absence
        fields = '__all__'
