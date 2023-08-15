from django.shortcuts import render, redirect
from .forms import EmployeeRegistrationForm

def register_employee(request):
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # Redirect to the employee list page
    else:
        form = EmployeeRegistrationForm()
    return render(request, 'registration/register_employee.html', {'form': form})
