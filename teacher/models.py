from django.db import models
from datetime import timedelta

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField()
    age = models.IntegerField(default=0)
    course= models.CharField(max_length=40,default=0)
    nationality = models.CharField(max_length = 40,default='Kenya')
    gender = models.CharField(max_length = 20)
    bio = models.TextField()
    national_id = models.PositiveBigIntegerField(default=0)
    years_of_experience = models.IntegerField(default=1)
    teaching_hours = models.DurationField(default=timedelta(minutes=60))
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
