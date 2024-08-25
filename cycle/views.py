from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Cycle
from datetime import datetime, timedelta


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
    febDate=[]
    marDate=[]
    aprDate=[]
    mayDate=[]
    junDate=[]
    julDate=[]
    augDate=[]
    sepDate=[]
    octDate=[]
    novDate=[]
    decDate=[]


    for x in range(1, 43):
        cycleAndDates.append({"cycleDate":cycles[x-1].date, "janDate":janDate[x-1], "caShift":cycles[x-1].aShift, "cbShift":cycles[x-1].bShift, "ccShift":cycles[x-1].cShift, "cdShift":cycles[x-1].dShift, "ceShift":cycles[x-1].eShift, "cfShift":cycles[x-1].fShift},)
    
    xd = datetime(2024,2,12,12,0,0)

    print('-----------Start-----------')
    print(xd-timedelta(days=42))
    print(calcDate(2024, 3))
    print('-----------end-----------')

    return render(request, 'cycle/cycle.html', {
        'cycles': cycles,
        'allDates': allDates,
        'cycleAndDates': cycleAndDates,
    })



def calcDate(yr, mnth):
    aDate = []
    for x in range(1, 43):
        try:
            aDate.append(datetime(yr,mnth,x,12,0,0))
        except:
            aDate.append('')

    return aDate
    