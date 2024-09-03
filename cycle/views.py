from django.shortcuts import render, redirect
from .models import Cycle
from datetime import datetime, timedelta
import math
from django.http import JsonResponse

# Create your views here.
def index(request):
    cycles = Cycle.objects.all()
    cycleAndDates = []
    yrs = 2024
    if request.method == 'GET':
        if 'yr' in request.GET:
            yrs = int(request.GET['yr'])

    janDate=calcDate(yrs,1)
    febDate=calcDate(yrs,2)
    marDate=calcDate(yrs,3)
    aprDate=calcDate(yrs,4)
    mayDate=calcDate(yrs,5)
    junDate=calcDate(yrs,6)
    julDate=calcDate(yrs,7)
    augDate=calcDate(yrs,8)
    sepDate=calcDate(yrs,9)
    octDate=calcDate(yrs,10)
    novDate=calcDate(yrs,11)
    decDate=calcDate(yrs,12)

    for x in range(1, 43):
        cycleAndDates.append({"cycleDate":cycles[x-1].date, "janDate":janDate[x-1], "febDate": febDate[x-1], "marDate": marDate[x-1], "aprDate": aprDate[x-1], "mayDate": mayDate[x-1], "junDate": junDate[x-1], "julDate": julDate[x-1], "augDate": augDate[x-1], "sepDate": sepDate[x-1], "octDate": octDate[x-1], "novDate": novDate[x-1], "decDate": decDate[x-1], "caShift":cycles[x-1].aShift, "cbShift":cycles[x-1].bShift, "ccShift":cycles[x-1].cShift, "cdShift":cycles[x-1].dShift, "ceShift":cycles[x-1].eShift, "cfShift":cycles[x-1].fShift},)
    
    return render(request, 'cycle/cycle.html', {
        'cycles': cycles,
        'yrs': yrs,
        'cycleAndDates': cycleAndDates,
    })



def calcDate(yr, mnth):
    aDate = []
    for x in range(1, 43):
        aDate.append('')

    finalMNTH = datetime(yr,mnth,1,12,0,0) - datetime(2024,1,1,12,0,0) 
    placeKeeper = finalMNTH.days - (math.trunc(finalMNTH.days / 42) * 42)

    for x in range(1, 43):
        try:
            aDate[placeKeeper] = datetime(yr,mnth,x,12,0,0)
            placeKeeper += 1
            if placeKeeper == 42:
                placeKeeper = 0
        except:
            aDate.append('')

    return aDate
    


def cycleAPI(request):
    cycles = Cycle.objects.all()
    cycleAndDates = []
    yrs = 2024
    if request.method == 'GET':
        if 'yr' in request.GET:
            yrs = int(request.GET['yr'])

    janDate=calcDate(yrs,1)
    febDate=calcDate(yrs,2)
    marDate=calcDate(yrs,3)
    aprDate=calcDate(yrs,4)
    mayDate=calcDate(yrs,5)
    junDate=calcDate(yrs,6)
    julDate=calcDate(yrs,7)
    augDate=calcDate(yrs,8)
    sepDate=calcDate(yrs,9)
    octDate=calcDate(yrs,10)
    novDate=calcDate(yrs,11)
    decDate=calcDate(yrs,12)

    for x in range(1, 43):
        cycleAndDates.append({"cycleDate":cycles[x-1].date, "janDate":janDate[x-1], "febDate": febDate[x-1], "marDate": marDate[x-1], "aprDate": aprDate[x-1], "mayDate": mayDate[x-1], "junDate": junDate[x-1], "julDate": julDate[x-1], "augDate": augDate[x-1], "sepDate": sepDate[x-1], "octDate": octDate[x-1], "novDate": novDate[x-1], "decDate": decDate[x-1], "caShift":cycles[x-1].aShift, "cbShift":cycles[x-1].bShift, "ccShift":cycles[x-1].cShift, "cdShift":cycles[x-1].dShift, "ceShift":cycles[x-1].eShift, "cfShift":cycles[x-1].fShift},)
    return JsonResponse(cycleAndDates, safe=False)