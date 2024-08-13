from django.db import models

# Create your models here.
class Class(models.Model):
      class_name= models.CharField(max_length=20).primary_key
      class_electronic_items = models.TextField()
      class_capacity = models.PositiveSmallIntegerField()
      class_motto = models.TextField(default=0)
      class_groups= models.TextField()
      no_of_tables = models.IntegerField(default=0)
      no_of_chairs = models.PositiveSmallIntegerField()
      class_lessons = models.TextField(default=0)
      class_student_representative = models.CharField(max_length=40,default='Ajema')
      class_size=models.CharField(max_length=40,default='medium')
      
      def __str__(self):
        return f"{self.class_name} {self.class_motto}"