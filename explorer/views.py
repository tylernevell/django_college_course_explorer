from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import DepartmentHead, Instructor, Course, Department
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'explorer/index.html'
    context_object_name = 'department_list'

    def get_queryset(self):
        return Department.objects.order_by('department_name')


class CourseListView(generic.DetailView):
    model = Department
    template_name = 'explorer/course_list.html'


class CourseView(generic.DetailView):
    model = Course
    template_name = 'explorer/course_view.html'


class InstructorView(generic.DetailView):
    model = Instructor
    template_name = 'explorer/instructor_view.html'

#def index(request):
    #department_list = Department.objects.order_by('department_name')
    #context = {
        #'department_list': department_list,
    #}
    #return render(request, 'explorer/index.html', context)


#def course_list(request, department_id):
    #department = get_object_or_404(Department, pk=department_id)
    #return render(request, 'explorer/course_list.html', {'department': department})


#def course_view(request, course_id):
    #course = get_object_or_404(Course, pk=course_id)
    #return render(request, 'explorer/course_view.html', {'course': course})


#def instructor_view(request, instructor_id):
    #response = "Below is the %s's information."
    #return HttpResponse(response % instructor_id)