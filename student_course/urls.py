# student_course/urls.py
from django.urls import path
from . import views
from .views import student_list, course_list, enroll_student

urlpatterns = [
    path('students/', student_list, name='student_list'),
    path('courses/', course_list, name='course_list'),
    path('enroll/', enroll_student, name='enroll_student'),  # URL for enrolling students
]
