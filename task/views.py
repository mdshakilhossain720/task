from django.shortcuts import render
from . forms import Regestion

# Create your views here.

def showfrom(request):
    frm=Regestion()
    return render(request,'forms.html',{'frm':frm})

