from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'manplan/manplan.html', {
        'counter': range(100),
    })
