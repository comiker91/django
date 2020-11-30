from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import *
# Create your views here.
def index(request):
    template = 'app1/base.html'
    tupel = ("Hans Dampf","Gut","lieber")
    tabelle = Tagebuch.objects.all().order_by("-bewertung")
    return render(request,template,{'parameter':tupel, 'tabelle': tabelle})

def tgbDetail(request, comment_id):
    # DS Lesen
    ds = Tagebuch.objects.get(id = comment_id)
    if request.method == "GET":
        print("Website wurde direkt aufgerufen")
        # Formular initialisieren
        template = 'app1/tgbdetail.html'
        return render(request, template, {'ds':ds,})        
    elif request.method == "POST":
        print("Website wurde durch ein Formular aufgerufen")
        print(request.POST)
        # Formular auslesen
        name = request.POST['tgbname']
        kommentar = request.POST['tgbkommentar']
        # DS ändern
        ds.name = name
        ds.kommentar = kommentar
        # DS Speichern
        ds.save()
        # Zur Liste zurückkehren
        return redirect("/")
    else:
        print("Da ist mächtig etwas schief gelaufen.")
    
