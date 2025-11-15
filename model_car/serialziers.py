from rest_framework import serializers
from .models import Cars

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields ="__all__"