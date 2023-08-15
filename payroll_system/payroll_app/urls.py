from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns
    path('register/', views.register_employee, name='register_employee'),
]
