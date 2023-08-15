from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=50, unique=True)  # Employee ID (can be barcode)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # Add other employee-related fields like contact info, position, etc.

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    clock_in = models.DateTimeField()
    clock_out = models.DateTimeField(null=True, blank=True)
    # You can add more fields like location, notes, etc.

class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()

class SalaryComponent(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # You can add more fields like type, frequency, etc.
