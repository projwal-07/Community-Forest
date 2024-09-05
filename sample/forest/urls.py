
from django.urls import path
from .import views

urlpatterns = [
    path('karyasamiti/',views.karyasamiti,name='karyasamiti'),
    path('salakarsamiti/',views.salakarsamiti,name='salakarsamiti'),
    path('lekhasamiti/',views.lekhasamiti,name='lekhasamiti'),
    path('tolesamiti/',views.tolesamiti,name='tolesamiti'),
    path('chetriyasamiti/',views.chetriyasamiti,name='chetriyasamiti'),
]
