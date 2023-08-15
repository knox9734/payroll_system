from django.shortcuts import render, redirect
from .forms import EmployeeRegistrationForm
from .models import Employee,Attendance
from datetime import datetime, date
from datetime import timedelta

def register_employee(request):
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/register_employee.html', {'form': form})
    else:
        form = EmployeeRegistrationForm()
    return render(request, 'registration/register_employee.html', {'form': form})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def mark_attendance(request):
    employees = Employee.objects.all()
    return render(request, 'employee_attendance_mark.html', {'employees': employees})

def toggle_attendance(request, employee_id):
    employee = Employee.objects.get(employee_id=employee_id)
    today = date.today()
    now = datetime.now()

    # Check if there is an attendance entry for today
    attendance = Attendance.objects.filter(employee=employee, clock_in__date=today).order_by('-clock_in').first()

    if attendance and not attendance.clock_out:
        # If there's an entry for today and clock_out is not set, mark as out
        attendance.clock_out = now
        attendance.save()
    else:
        # Otherwise, mark as in
        Attendance.objects.create(employee=employee, clock_in=now)

    return redirect('mark_attendance')

def view_attendance(request, employee_id):
    employee = Employee.objects.get(employee_id=employee_id)
    attendance_records = Attendance.objects.filter(employee=employee)
    
    attendance_info = []
    total_hours_worked = timedelta(hours=0)

    # Iterate through attendance records to calculate total hours worked
    for i in range(len(attendance_records) - 1):
        current_record = attendance_records[i]
        next_record = attendance_records[i + 1]

        if current_record.clock_out and next_record.clock_in:
            hours_worked = next_record.clock_in - current_record.clock_out
            total_hours_worked += hours_worked
            attendance_info.append((current_record, next_record, hours_worked))

    total_hours = total_hours_worked.seconds // 3600
    total_minutes = (total_hours_worked.seconds // 60) % 60

    return render(request, 'view_attendance.html', {
        'employee': employee,
        'attendance_info': attendance_info,
        'total_hours': total_hours,
        'total_minutes': total_minutes
    })