from django.urls import path

from . import views

app_name ='calcu2/'

urlpatterns = [
    # ex: /encuesta/
    path('', views.index, name='index'),
    path('/resultado', views.resultado, name='resultado'),
]