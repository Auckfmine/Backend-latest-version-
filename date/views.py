from django.shortcuts import render

from rest_framework import viewsets
from .models import date
from .serializers import DateSerializer







class DateView(viewsets.ModelViewSet):
    queryset = date.objects.all()
    serializer_class = DateSerializer
    
    
# Create your views here.
