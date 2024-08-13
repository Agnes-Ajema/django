from django.db import models

# Create your models here.

class Courses(models.Model):
    courses = models.CharField(max_length=80)

class Student(models.Model):
    courses = models.ManyToManyField(Courses)
    student_name = models.CharField(max_length = 40,default='Ajema')
    student_bio = models.TextField()
    student_email = models.EmailField()
    date_of_birth = models.DateField()
    student_code = models.PositiveSmallIntegerField()
    student_nationality = models.CharField(max_length = 25,default='Kenya')
    student_guardian = models.CharField(max_length = 40,default=0)
    student_locker= models.IntegerField()
    student_class= models.CharField(max_length = 40,default=0)
    student_mentor = models.CharField(max_length = 40,default=0)


    
    def __str__(self):
        return f"{self.student_name} {self.student_bio}"
    
    