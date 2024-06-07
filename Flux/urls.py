from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from devices.views import CollectedDataViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'data',CollectedDataViewset)

def home(request):
    return render(request, 'main.html')

urlpatterns = [
    path('', home, name='home' ),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
