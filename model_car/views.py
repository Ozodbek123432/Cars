from rest_framework import generics
from .models import Cars
from .serialziers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

class PersonCrud(ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = StudentSerializer
