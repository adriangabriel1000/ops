from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    quals = "abcd"
    return render(request, 'home/index.html', {
        'quals': quals,
    })