from django.db import models

class Cars(models.Model):
    car_name = models.CharField(max_length=100)
    car_year = models.IntegerField()
    car_color = models.CharField(max_length=100)
    car_speed = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
