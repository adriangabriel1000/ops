from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Cycle
from datetime import datetime


# Create your views here.
def index(request):
    cycles = Cycle.objects.all()
    if request.method == 'POST':
        datesFor2024 = []
        y=1
        z=0
        if 'btn24' in request.POST:
            for x in range(1, 42): #42
                z+=1
                if x > 30:
                    z=1
                dt = {x: datetime(2024,y,z,12,0,0)}
                datesFor2024.append(dt)
                if x == 32:
                    y += 1
            #datesFor2024 = {'1': datetime(2024,1,1,12,0,0), '2': datetime(2024,1,2,12,0,0)}
            #dates24 = datetime(2024,1,1,12,0,0)
            #print(request.POST['btn24'])
            print(datesFor2024)
        print("posting")

    return render(request, 'cycle/cycle.html', {
        'cycles': cycles,


    })