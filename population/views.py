from django.shortcuts import render
from .models import Population
from .serializers import PopulationSerializer
from rest_framework import viewsets
# Create your views here.

class PopulationView(viewsets.ModelViewSet):
    queryset = Population.objects.all()
    serializer_class = PopulationSerializer
