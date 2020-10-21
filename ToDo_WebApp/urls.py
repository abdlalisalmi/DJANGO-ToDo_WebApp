from django.contrib import admin
from django.urls import path

from .views import homePage

urlpatterns = [
    path('', homePage, name='homePage'),

    path('admin/', admin.site.urls),
]
