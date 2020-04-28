import datetime
from django.db import models
from django.utils import timezone
# Create your models here.


class Department(models.Model):
    department_name = models.CharField(max_length=100)
    # head_of = models.ForeignKey('Instructor', on_delete=models.CASCADE, blank=True)


# class Course(models.Model):
    # belongs_to = models.ForeignKey(Department, on_delete=models.CASCADE)
    # course_name = models.CharField(max_length=100)
    # course_number = models.
    # pub_date = models.DateTimeField('Date of Course Publication')

    # def __str__(self):
        # return self.course_name


class Instructor(models.Model):
    belongs_to = models.ForeignKey(Department, on_delete=models.CASCADE)
    # teaches = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor_name = models.CharField(max_length=100)
    # head_of = models.OneToOneField(Department, on_delete=models.SET_NULL, null=True, blank=True)


# need to have a table for