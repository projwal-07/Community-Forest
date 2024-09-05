from django.shortcuts import render
from .models import Karya_Samiti_Member,Chetriya_Samiti_Member,Lekha_Samiti_Member,Salakar_Samiti_Member,Tole_Samiti_Member

# Create your views here.
def karyasamiti(request):
    karyamembers= Karya_Samiti_Member.objects.all()
    return render(request,'karyasamiti.html',{'karyamembers':karyamembers})

def tolesamiti(request):
    tolemembers= Tole_Samiti_Member.objects.all()
    return render(request,'tolesamiti.html',{'tolemembers':tolemembers})

def lekhasamiti(request):
    lekhamembers= Lekha_Samiti_Member.objects.all()
    return render(request,'lekhasamiti.html',{'lekhamembers':lekhamembers})

def salakarsamiti(request):
    salakarmembers= Salakar_Samiti_Member.objects.all()
    return render(request,'salakarsamiti.html',{'salakarmembers':salakarmembers})

def chetriyasamiti(request):
    chetriyamembers= Chetriya_Samiti_Member.objects.all()
    return render(request,'chetriyasamiti.html',{'chetriyamembers':chetriyamembers})