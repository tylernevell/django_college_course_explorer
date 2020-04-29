import datetime
from django.db import models
from django.utils import timezone
# Create your models here.


class Department(models.Model):
    department_name = models.CharField(max_length=100)
    # head_of = models.ForeignKey('Instructor', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.department_name


class Course(models.Model):
    belongs_to = models.ForeignKey(Department, on_delete=models.CASCADE)
    taught_by = models.ForeignKey('Instructor', on_delete=models.SET_NULL, null=True)
    course_name = models.CharField(max_length=110)
    # course_number = models.
    # pub_date = models.DateTimeField('Date of Course Publication')

    def __str__(self):
        return self.course_name


class Instructor(models.Model):
    belongs_to = models.ForeignKey(Department, on_delete=models.CASCADE)
    #teaches = models.ManyToManyField(Course)
    instructor_name = models.CharField(max_length=100)
    # head_of = models.OneToOneField(Department, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.instructor_name


class DepartmentHead(models.Model):
    name = models.OneToOneField(Department, on_delete=models.SET_NULL, null=True)
    headed_by = models.OneToOneField(Instructor, on_delete=models.SET_NULL, null=True)

# need to have a table for