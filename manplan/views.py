from django.shortcuts import render, redirect
from .models import *
import string
import random
from datetime import datetime, timedelta, timezone
from collections import Counter
import operator 


# Create your views here.
def index(request):
    employees = Employee.objects.all()
    schedules = Schedule.objects.all()
    aSh = Schedule.objects.filter(employee__shift__contains='A') #filter(employee__shift__contains='A', date__contains=datetime.today().date())
    aEmployees = Employee.objects.filter(shift='A')
    bEmployees = Employee.objects.filter(shift='B')
    cEmployees = Employee.objects.filter(shift='C')
    dEmployees = Employee.objects.filter(shift='D')
    eEmployees = Employee.objects.filter(shift='E')
    fEmployees = Employee.objects.filter(shift='F')
    oEmployees = Employee.objects.filter(shift='O')
    aList = {}

    # for sh in aSh:
    #     print(sh.employee)
    aTemp = []
    dateList = []
    for x in range(-7,42):
        dateList.append(datetime.today().date() + timedelta(x))

# ------------ A Shift ---------------------------------------
    
    aEmpCount = {}
    for emp in aEmployees:
        aEmpCount.update({emp.name: Schedule.objects.filter(employee__name__contains=emp).count()})


    

    # print(aEmpCount)
    # print(aEmpCount.get('Hairy Potter'))
    # print(Schedule.objects.filter(employee__name__contains='Hairy Potter').count())

    # print(aSh.values_list('employee'))                
    empShList = []
    # for a in aSh:
    #     empShList.append(str(a.employee))

    # print(operator.countOf(empShList, 'Hairy Potter'))
    # print(sum('Hairy Potter' in str(a.employee) for a in aSh))
    counter = 0
    for emp in aEmployees:
        counter = aEmpCount.get(emp.name)
        for a in aSh:
            
            if a.employee == emp:
                for date in dateList:
                    if a.date.date() == date:
                        if a.employee == emp:
                            aTemp.append(a.position)
                    else:
                        aTemp.append(' ')

            

        aList.update({emp: aTemp}) 
        aTemp=[]
                    

    # print(aList)
    
#---------------------- End A Shift ----------------------------------
        

    return render(request, 'manplan/manplan.html', {
        'counter': range(49),
        'employees': employees,
        'aEmployees': aEmployees,
        'bEmployees': bEmployees,
        'cEmployees': cEmployees,
        'dEmployees': dEmployees,
        'eEmployees': eEmployees,
        'fEmployees': fEmployees,
        'oEmployees': oEmployees,
        'dateList': dateList,
        'aList': aList,
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