from django.shortcuts import render, redirect
from .models import *
from cycle.models import Cycle
from datetime import datetime, timedelta
import string
import random
import math
import calendar
import random


# Create your views here.
def index(request):
    dateList = []
    counter = {}
    cnt = 1
    for x in range(-7,42):
        dateList.append(datetime.today().date() + timedelta(x))
        daysmnth = calendar.monthrange((datetime.today().date() + timedelta(x)).year, (datetime.today().date() + timedelta(x)).month)[1]
        if (datetime.today().date() + timedelta(x)).day == daysmnth or x == 41:
            counter.update({((datetime.today().date() + timedelta(x)).strftime('%B')): cnt})
            cnt = 0      
        cnt += 1

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
    popRemainder(plan('A', dateList), aCycle, dateList)


    return render(request, 'manplan/manplan.html', {
        'counter': counter,
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
    for x in range(1, 30):
        name = ''.join(random.choices(string.ascii_letters, k=random.randint(6, 10)))
        surname = ''.join(random.choices(string.ascii_letters, k=random.randint(7, 15)))
        fullname = name + ' ' + surname
        Employee.objects.create(name=fullname, shift='O')
        print(fullname)

    return employee

# Populate the rest of the table
def plan(shft, dlist):
    aTemp = []
    aList = {}

    for emp in Employee.objects.filter(shift=shft):
        tempEmp = {}
        empTemp = {}
        tempEmp = Schedule.objects.filter(employee=emp)
        for tem in tempEmp:
            empTemp.update({tem.date.date(): tem.position})

        aTemp.append(emp.ftm)

        for date in dlist:
            if date in empTemp:
                aTemp.append(empTemp[date])
            else:
                aTemp.append(' ')
        aList.update({emp: aTemp})
        aTemp=[]    
    return aList

# Populate the Entire Manplan
def popRemainder(pos, shft, date):

    for p in pos.values():
        print(p[10])


# Populate Random Positions on Manplan
def randPos():
    for x in range(1,100):
        if (datetime.today().date() + timedelta(-7)).day > (datetime.today().date() + timedelta(41)).day:
            rndDay = random.randint((datetime.today().date() + timedelta(42)).day, (datetime.today().date() + timedelta(-7)).day)
        else:
            rndDay = random.randint((datetime.today().date() + timedelta(-7)).day, (datetime.today().date() + timedelta(41)).day)

        if (datetime.today().date() + timedelta(-7)).month > (datetime.today().date() + timedelta(41)).month:
            rndMnth = random.randint((datetime.today().date() + timedelta(41)).month, (datetime.today().date() + timedelta(-7)).month)
        else:
            rndMnth = random.randint((datetime.today().date() + timedelta(-7)).month, (datetime.today().date() + timedelta(41)).month)

        rndYr = 2024

        posi = ['T1M', 'N1M', '0M', 'SNM', 'T1A', 'N1A', '0A', 'SNA', 'T1N', 'N1N', '0N', 'SNN']
        rndPos = random.choice(posi)

        nms = []
        for a in Employee.objects.all():
            nms.append(a.pk)
        rndNme = random.choice(nms)

        Schedule.objects.create(date=datetime(rndYr, rndMnth, rndDay, 12, 0, 0), position=rndPos, employee_id=rndNme)
