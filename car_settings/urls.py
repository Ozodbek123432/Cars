from django.contrib import admin
from django.urls import path, include
from model_car.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list', PersonCrud.as_view({'get': 'list'})),
    path('create/', PersonCrud.as_view({'post':'create'}),name='creat'),
    path('update/<int:pk>/', PersonCrud.as_view({'put':'update'}),name='update'),
    path('delete/<int:pk>/', PersonCrud.as_view({'delete':'delete'}),name='delete'),
]