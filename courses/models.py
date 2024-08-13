from django.db import models

# Create your models here.
class Courses(models.Model):
    course_name = models.CharField(max_length = 40).primary_key
    trainer = models.CharField(max_length=40,default=0)
    duration = models.IntegerField()
    number_of_assessments = models.IntegerField(default=0)
    syllabus = models.CharField(max_length=40,default=0)
    number_of_assignments = models.IntegerField(default=0)
    course_id = models.PositiveSmallIntegerField()
    description = models.TextField(default='course')
    requirements= models.CharField(max_length=40,default=0)
    teaching_materials = models.TextField()
    
    
    def __str__(self):
        
        return f"{self.course_name} {self.trainer}"
    
