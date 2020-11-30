from django.shortcuts import render
from django.http import HttpResponse

from .models import *
# Create your views here.
def index(request):
    template = 'app1/base.html'
    tupel = ("Hans Dampf","Gut","lieber")
    tabelle = Tagebuch.objects.all()
    print(tabelle)
    return render(request,template,{'parameter':tupel, 'tabelle': tabelle})