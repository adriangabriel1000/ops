from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Cycle
from datetime import datetime, timedelta
import calendar


# Create your views here.
def index(request):
    cycles = Cycle.objects.all()
    allDates = []
    cycleAndDates = []
    if request.method == 'POST':
        datesFor2024 = []
        y=1
        z=0
        if 'btn24' in request.POST:
            for x in range(1, 43): #42
                z+=1
                if x == 32:
                    z=1
                    y += 1
                dt = {x: datetime(2024,y,z,12,0,0)}
                datesFor2024.append(dt)

        print('Posted!!')
    
    y = 1
    z = 1
    
    # Append 42 iterations of sequential datetime starting 01 Jan 2024
    for x in range(1, 43): 
        if x == 32:
            y += 1
            z = 1
        allDates.append(datetime(2024,y,z,12,0,0))
        z+=1

    # Making janDate

    janDate=calcDate(2024,1)
    febDate=calcDate(2024,2)
    marDate=calcDate(2024,3)
    aprDate=calcDate(2024,4)
    mayDate=calcDate(2024,5)
    junDate=calcDate(2024,6)
    julDate=[]
    augDate=[]
    sepDate=[]
    octDate=[]
    novDate=[]
    decDate=[]


    for x in range(1, 43):
        cycleAndDates.append({"cycleDate":cycles[x-1].date, "janDate":janDate[x-1], "febDate": febDate[x-1], "marDate": marDate[x-1], "aprDate": aprDate[x-1], "mayDate": mayDate[x-1], "junDate": junDate[x-1], "caShift":cycles[x-1].aShift, "cbShift":cycles[x-1].bShift, "ccShift":cycles[x-1].cShift, "cdShift":cycles[x-1].dShift, "ceShift":cycles[x-1].eShift, "cfShift":cycles[x-1].fShift},)
    
    xd = datetime(2024,2,12,12,0,0)

    # print('-----------Start-----------')
    # # print(xd-timedelta(days=42))
    # # print(calcDate(2024, 3))
    # print('-----------end-----------')

    return render(request, 'cycle/cycle.html', {
        'cycles': cycles,
        'allDates': allDates,
        'cycleAndDates': cycleAndDates,
    })



def calcDate(yr, mnth):
    aDate = []
    # print(calendar.monthrange(yr, mnth)[1])
    print('----------' + str(mnth) + '-----------')
    if yr == 2024 and mnth == 1:
        for x in range(1, 43):
            try:
                aDate.append(datetime(yr,mnth,x,12,0,0))
            except:
                aDate.append('')
    else:
        #dateMulti = ((mnth - 1) * 42) - calendar.monthrange(yr, mnth-1)[1]+1 #month 2= 42-31=11, 3=44-30=14
        dateMulti = datetime(yr,1,1,12,0,0) + timedelta(days=((mnth - 1) * 42))
        dateMultiA = int(dateMulti.day)
        monthMulti = int(dateMulti.month) - mnth
        if monthMulti == 1:
            finalMNTH = datetime(yr,5,1,12,0,0) - datetime(yr,1,1,12,0,0) 
            print(finalMNTH.days)
            print('PlaceKeeper = ' + str((42*5) - finalMNTH.days))
        dateMultiB = 1
        stoBeginingVal = 42 - (dateMultiA - 1)
        # print(stoBeginingVal)
        # print(dateMulti.day+1)
        #print(dateMultiB)
 
        for x in range(1, 43):
            try:
                aDate.append(datetime(yr,mnth,dateMultiA,12,0,0))
                dateMultiA += 1
                # print(dateMultiA)

            except:
                if x > stoBeginingVal: #int(calendar.monthrange(yr, mnth-1)[1]):
                    aDate.append(datetime(yr,mnth,dateMultiB,12,0,0))
                    dateMultiB += 1
                    # print(calendar.monthrange(yr, mnth-1)[1])
                else:
                    aDate.append('')
 
            
            

    return aDate
    