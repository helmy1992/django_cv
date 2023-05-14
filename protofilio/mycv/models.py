from django.db import models
class Student(models.Model):
    f_name= models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)

class courses(models.Model):
    course1 = models.CharField(max_length=255)
    course2 = models.CharField(max_length=255)
