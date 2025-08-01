from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
# Create your views here.
def employee_detail(request, empId):
  try:
    employee = Employee.objects.get(pk=empId)
    context = {'employee': employee}
    return render(request, "employee_detail.html", context)
  except Employee.DoesNotExist:
    return HttpResponse("Employee not found")