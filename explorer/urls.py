from django.urls import path

from . import views

app_name = 'explorer'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.CourseListView.as_view(), name='Course List'),
    path('<int:pk>/course_view/', views.CourseView.as_view(), name='Course View'),
    path('<int:pk>/instructor_view/', views.InstructorView.as_view(), name='Instructor'),
    #path('', views.index, name='index'),
    #path('<str:department_id>/', views.course_list, name='Course List'),
    #path('<int:course_id>/course_view/', views.course_view, name='Course View'),
    #path('<int:instructor_id>/instructor_view/', views.instructor_view, name='Instructor'),
]