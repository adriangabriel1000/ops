from django.urls import path
from . import views

app_name = 'cycle'
urlpatterns = [
    path('', views.index, name='cycle'),
    

]