from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *


class CultureListApiView(ModelViewSet):
    queryset = Culture.objects.all()
    serializer_class = CultureSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class FarmerListApiView(ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
    search_fields = ['name']


class PlotListApiView(ModelViewSet):
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['farmer.name']


class SeasonListApiView(ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer




