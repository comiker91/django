from django.shortcuts import render
from django.http import HttpResponse

from .models import *
# Create your views here.
def index(request):
    template = 'app1/base.html'
    tupel = ("Hans Dampf","Gut","lieber")
    tabelle = Tagebuch.objects.all().order_by("-bewertung")
    return render(request,template,{'parameter':tupel, 'tabelle': tabelle})

def tgbDetail(request, comment_id):
    if request.method == "GET":
        print("Website wurde direkt aufgerufen")
    elif request.method == "POST":
        print("Website wurde durch ein Formular aufgerufen")
    else:
        print("Da ist mächtig etwas schief gelaufen.")
    
    ds = Tagebuch.objects.get(id = comment_id)
    template = 'app1/tgbdetail.html'
    return render(request, template, {'ds':ds,})