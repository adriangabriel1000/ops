from django.urls import path
from . import views

app_name = 'manplan'
urlpatterns = [
    path('', views.index, name='manplanIndex'),

]