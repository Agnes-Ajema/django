from rest_framework import serializers
from student.models import Student
from classes.models import Class
from classroom_period.models import ClassroomPeriod
from courses.models import Courses
from teacher.models import Teacher

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class MinimalStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["student_name","student_email"]

class MinimalClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ["class_name"]

class MinimalClassroomPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassroomPeriod
        fields = ["classroom"] 

class MinimalCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ["course_name"]  

class MinimalTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["first_name", "last_name"] 
        
class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Class
        fields="__all__"
        
class ClassroomPeriodSerializer(serializers.ModelSerializer):
  class Meta:
    model=ClassroomPeriod
    fields="__all__"
    
class CoursesSerializer(serializers.ModelSerializer):
 class Meta:
    model=Courses
    fields = "__all__"
    
class TeacherSerializer(serializers.ModelSerializer):
 class Meta:
    model=Teacher
    fields = "__all__"
    
