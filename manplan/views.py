from django.shortcuts import render, redirect
from .models import *
from cycle.models import Cycle
import string
import random
import math
from datetime import datetime, timedelta


# Create your views here.
def index(request):
    dateList = []
    for x in range(-7,42):
        dateList.append(datetime.today().date() + timedelta(x))

    # --------------- Calculate Shift Cycle
    aCycle = []
    bCycle = []
    cCycle = []
    dCycle = []
    eCycle = []
    fCycle = []
    ref = 0
    for date in dateList:
        finalMNTH = date - datetime(2024,1,1,12,0,0).date() 
        ref = finalMNTH.days - (math.trunc(finalMNTH.days / 42) * 42) + 3
        aCycle.append((Cycle.objects.filter(id=ref).values('aShift')[0]['aShift']))
        bCycle.append((Cycle.objects.filter(id=ref).values('bShift')[0]['bShift']))
        cCycle.append((Cycle.objects.filter(id=ref).values('cShift')[0]['cShift']))
        dCycle.append((Cycle.objects.filter(id=ref).values('dShift')[0]['dShift']))
        eCycle.append((Cycle.objects.filter(id=ref).values('eShift')[0]['eShift']))
        fCycle.append((Cycle.objects.filter(id=ref).values('fShift')[0]['fShift']))
    # --------------- End Calculate Shift Cycle

    return render(request, 'manplan/manplan.html', {
        'counter': range(49),
        'dateList': dateList,
        'aList': plan('A', dateList),
        'bList': plan('B', dateList),
        'cList': plan('C', dateList),
        'dList': plan('D', dateList),
        'eList': plan('E', dateList),
        'fList': plan('F', dateList),
        'oList': plan('O', dateList),
        'aCycle': aCycle,
        'bCycle': bCycle,
        'cCycle': cCycle,
        'dCycle': dCycle,
        'eCycle': eCycle,
        'fCycle': fCycle,
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


def plan(shft, dlist):
    aTemp = []
    aEmpCount = {}
    aList = {}
    for emp in Employee.objects.filter(shift=shft):
        aEmpCount.update({emp.name: Schedule.objects.filter(employee__name__contains=emp).count()})

    for emp in Employee.objects.filter(shift=shft):
        tempEmp = {}
        empTemp = {}
        tempEmp = Schedule.objects.filter(employee=emp)
        for tem in tempEmp:
            empTemp.update({tem.date.date(): tem.position})

        for date in dlist:
            if date in empTemp:
                aTemp.append(empTemp[date])
            else:
                aTemp.append(' ')
    
        aList.update({emp: aTemp}) 
        aTemp=[]    
    return aList