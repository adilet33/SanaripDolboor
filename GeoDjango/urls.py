from django.contrib import admin
from django.urls import path, include

from agro.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'plot', PlotListApiView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/p1/', include(router.urls)),
]
