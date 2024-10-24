from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.timezone import utc
from .models import *
from cycle.models import Cycle
from datetime import datetime, timedelta
from django.core.paginator import Paginator
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
    for x in range(-7,407):#range(-7,42):
        dateList.append(datetime.today().date() + timedelta(x))
        daysmnth = calendar.monthrange((datetime.today().date() + timedelta(x)).year, (datetime.today().date() + timedelta(x)).month)[1]
        # print(daysmnth)
        if (datetime.today().date() + timedelta(x)).day == daysmnth:
            counter.update({((datetime.today().date() + timedelta(x)).strftime('%B')): cnt})
            cnt = 0      
        cnt += 1
    # print(counter)
    
    # --------------- Update Positions
    if request.method == 'POST':
        if 'csrfmiddlewaretoken' not in str(request.body.decode("utf8")):
            cellAddress = request.body.decode("utf8").split(",")
            if cellAddress[2] != 'null':
                empl = changePosition(cellAddress[0])
                Schedule.objects.create(date=datetime.combine(dateList[int(cellAddress[1])-1], datetime.min.time()).replace(tzinfo=utc), position=cellAddress[2], employee=empl) 
        
        if request.POST.get("backward"):
            print('Backward')

        if request.POST.get("forward"):
            print('Forward')

    
    paginator = Paginator(dateList, 49)
    page = request.GET.get('page')
    # print(dateList, page)
    dateList = paginator.get_page(page)
    counter = counterList(dateList, page)
    
    # print(page)


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



    return render(request, 'manplan/manplan.html', {
        'counter': counter,
        'cnt': range(1,50),
        'dateList': dateList,
        # 'tempList': tempList,
        'aList': expandedManplan('A', dateList, aCycle),
        'bList': expandedManplan('B', dateList, bCycle),
        'cList': expandedManplan('C', dateList, cCycle),
        'dList': expandedManplan('D', dateList, dCycle),
        'eList': expandedManplan('E', dateList, eCycle),
        'fList': expandedManplan('F', dateList, fCycle),
        'oList': expandedManplan('O', dateList),
        'aCycle': aCycle,
        'bCycle': bCycle,
        'cCycle': cCycle,
        'dCycle': dCycle,
        'eCycle': eCycle,
        'fCycle': fCycle,
    })

def counterList(dateList, page):
    counter = {}
    # for date in dateList:
    counter.update({'October': 15, 'November': 30, 'December': 4})
        # print(date, page)
    return counter


def changePosition(cellRow):
    aEmpl = Employee.objects.filter(shift='A')
    bEmpl = Employee.objects.filter(shift='B')
    cEmpl = Employee.objects.filter(shift='C')
    dEmpl = Employee.objects.filter(shift='D')
    eEmpl = Employee.objects.filter(shift='E')
    fEmpl = Employee.objects.filter(shift='F')
    oEmpl = Employee.objects.filter(shift='O')
    empl = ''

    a = aEmpl.count()
    b = bEmpl.count() + 1 + a
    c = cEmpl.count() + 1 + b
    d = dEmpl.count() + 1 + c
    e = eEmpl.count() + 1 + d
    f = fEmpl.count() + 1 + e
    o = oEmpl.count() + 1 + f
    if int(cellRow) > 0 and int(cellRow) <= a:
        empl = aEmpl[int(cellRow)-1]
    if int(cellRow) > a and int(cellRow) <= b:
        empl = bEmpl[int(cellRow) - a - 2]
    if int(cellRow) > b and int(cellRow) <= c:
        empl = cEmpl[int(cellRow) - b - 2]
    if int(cellRow) > c and int(cellRow) <= d:
        empl = dEmpl[int(cellRow) - c - 2]
    if int(cellRow) > d and int(cellRow) <= e:
        empl = eEmpl[int(cellRow) - d - 2]
    if int(cellRow) > e and int(cellRow) <= f:
        empl = fEmpl[int(cellRow) - d - 2]
    if int(cellRow) > f and int(cellRow) <= o:
        empl = oEmpl[int(cellRow) - f - 2]
    return empl



# Populate the rest of the table
# def plan(shft, dlist):
#     aTemp = []
#     aList = {}

#     for emp in Employee.objects.filter(shift=shft):
#         tempEmp = {}
#         empTemp = {}
#         tempEmp = Schedule.objects.filter(employee=emp)
#         for tem in tempEmp:
#             empTemp.update({tem.date.date(): tem.position})

#         aTemp.append(emp.ftm)

#         for date in dlist:
#             if date in empTemp:
#                 aTemp.append(empTemp[date])
#             else:
#                 aTemp.append(' ')
#         aList.update({emp: aTemp})
#         aTemp=[]    
#     return aList

# Populate the Entire Manplan ---------------- Incomplete
# def popRemainder(pos, shft, date):

#     y=0
#     for p in pos.values():
#         # print(p[10])
#         y += 1
#         doneList = [] 
       
#         for x in p:
#             doneList.append(x)
#             # print(x)

#         if y == 1:
#             break  
#     y=0 
#     addPos = " "
#     for pos in doneList:
#         if y > 0:
#             if pos != " ":
#                 addPos = pos
#             else:
#                 doneList[y] = addPos
#         y += 1

#     print(doneList)

def expandedManplan(shift, dateList, cycle=None):
    empPos = []
    finalList = {}
    positions = ['OJ', 'CO', 'PN', 'SN', '0', 'T1', 'T2', 'N1', 'N2', 'A1', 'A2', 'S1', 'S2', '1', '2', 'SM', 'X']
    for emp in Employee.objects.filter(shift=shift):
        shftEmp = {}
        getEmp = {}
        tmpPos = ""
        actualPos = []
        shftEmp = Schedule.objects.filter(employee=emp)

        if shift != 'O':
            for empl in reversed(shftEmp):
                if (dateList[0]) == empl.date.date():
                    tmpPos = empl.position
                else:
                    for t in range(0, -42, -1):
                        if (dateList[0] + timedelta(t)) == empl.date.date():
                            tmpPos = empl.position                
                            break
                        else:
                            tmpPos = ""
                        
        for tem in shftEmp:
            getEmp.update({tem.date.date(): tem.position})

        empPos.append(emp.ftm)    

        for date in dateList:
            for empl in shftEmp:
                if date == empl.date.date():
                    b=1
                    break
                else:
                    b=0
            if b == 1:
                actualPos.append('1')
            else:
                actualPos.append('')

        for date in dateList:
            if date in getEmp:
                empPos.append(getEmp[date])

                if shift != 'O':
                    tmpPos = getEmp[date]
            else:
                empPos.append(tmpPos)

        if cycle is not None:
            for i in range(0, 49):
                if (cycle[i] == '' or empPos[i+1] == '' or cycle[i] == 'T' or cycle[i] == 'S') and actualPos[i] == '':
                    empPos[i+1] = ""
                else:
                    if empPos[i+1] == "":
                        if empPos[i+1][:-1] in positions:
                            empPos[i+1] = empPos[i+1][:-1] + cycle[i]
                        else:
                            empPos[i+1] = empPos[i+1]

        finalList.update({emp: empPos})
        empPos=[]  
    return finalList







# Populate Employee Model with Random Characters  ---------------- Run when required
def pop():
    employee = Employee.objects.all()
    for x in range(1, 30):
        name = ''.join(random.choices(string.ascii_letters, k=random.randint(6, 10)))
        surname = ''.join(random.choices(string.ascii_letters, k=random.randint(7, 15)))
        fullname = name + ' ' + surname
        Employee.objects.create(name=fullname, shift='O')
        print(fullname)
    return employee


# Populate Random Positions on Manplan ---------------- Run when required
def randPos():
    for x in range(1,100):
        rndDt = random.randint(-7, 41)
        rndDay = (datetime.today().date() + timedelta(rndDt)).day
        rndMnth = (datetime.today().date() + timedelta(rndDt)).month
        rndYr = 2024
        rndDate = datetime(rndYr, rndMnth, rndDay, 12, 0, 0)
        posi = ['T1M', 'N1M', '0M', 'SNM', 'T1A', 'N1A', '0A', 'SNA', 'T1N', 'N1N', '0N', 'SNN']
        rndPos = random.choice(posi)
        nms = []
        for a in Employee.objects.all():
            nms.append(a.pk)
        rndNme = random.choice(nms)
        Schedule.objects.create(date=rndDate, position=rndPos, employee_id=rndNme)
