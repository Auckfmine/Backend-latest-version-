from rest_framework.views import APIView
from rest_framework import generics
from .models import Absence
from .seralizers import AbsenceSerializer



class AbsenceViews(generics.ListCreateAPIView):
    queryset = Absence.objects.all()
    serializer_class = AbsenceSerializer

# Create your views here.
