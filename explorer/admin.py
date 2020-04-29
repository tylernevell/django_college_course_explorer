from django.contrib import admin
from .models import Instructor, Course, Department, DepartmentHead
# Register your models here.
admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(DepartmentHead)