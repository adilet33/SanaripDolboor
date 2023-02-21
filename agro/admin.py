from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import *


@admin.register(Culture)
class CultureAdmin(OSMGeoAdmin):
    list_display = ('name',)


@admin.register(Farmer)
class FarmerAdmin(OSMGeoAdmin):
    list_display = ('name',)


@admin.register(Plot)
class PlotAdmin(OSMGeoAdmin):
    list_display = ('contour', 'farmer', 'culture', 'seasons')


@admin.register(Season)
class SeasonAdmin(OSMGeoAdmin):
    list_display = ('name',)
