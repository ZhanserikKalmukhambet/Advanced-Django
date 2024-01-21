from django.urls import path
from .views import student_list, student_detail


urlpatterns = [
    path('students/', student_list),
    path('students/<int:pk>', student_detail)
    # path('add/', add_student, name='add'),
]