from django.contrib import admin
from django.urls import path
from model_car.models import Cars
from model_car.views import *
urlpatterns = [

    path('admin/', admin.site.urls),
    path('crate/',CarsFunction.as_view(),name='crate'),
    path('delet/',CarsView.as_view(),name='delete'),

]