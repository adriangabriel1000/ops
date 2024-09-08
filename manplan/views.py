from django.shortcuts import render, redirect
from .models import *
import string
import random

# Create your views here.
def index(request):
    employees = Employee.objects.all()
    aEmployees = Employee.objects.filter(shift='A')
    bEmployees = Employee.objects.filter(shift='B')
    cEmployees = Employee.objects.filter(shift='C')
    dEmployees = Employee.objects.filter(shift='D')
    eEmployees = Employee.objects.filter(shift='E')
    fEmployees = Employee.objects.filter(shift='F')
    oEmployees = Employee.objects.filter(shift='O')
    print(aEmployees)
    return render(request, 'manplan/manplan.html', {
        'counter': range(100),
        'employees': employees,
        'aEmployees': aEmployees,
        'bEmployees': bEmployees,
        'cEmployees': cEmployees,
        'dEmployees': dEmployees,
        'eEmployees': eEmployees,
        'fEmployees': fEmployees,
        'oEmployees': oEmployees,
    })






# Populate Employee Model with Random Characters
def pop():
    employee = Employee.objects.all()
    schedule = Schedule.objects.all()
    for x in range(1, 30):
        name = ''.join(random.choices(string.ascii_letters, k=random.randint(6, 10)))
        surname = ''.join(random.choices(string.ascii_letters, k=random.randint(7, 15)))
        fullname = name + ' ' + surname
        Employee.objects.create(name=fullname, shift='O')
        print(fullname)

    return employee