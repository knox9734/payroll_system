from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns
    path('register/', views.register_employee, name='register_employee'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('toggle_attendance/<str:employee_id>/', views.toggle_attendance, name='toggle_attendance'),
    path('view_attendance/<str:employee_id>/', views.view_attendance, name='view_attendance'),
    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
]
