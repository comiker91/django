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
    tabelleBewertung = Bewertung.objects.all().order_by("wert")
    if request.method == "GET":
        # Formular initialisieren
        template = 'app1/tgbdetail.html'
        return render(request, template, {'ds':ds,'tabbew': tabelleBewertung})        
    elif request.method == "POST":
        # Formular auslesen
        name = request.POST['tgbname']
        kommentar = request.POST['tgbkommentar']
        bewertung = request.POST['tgbbewertung']
        # DS ändern
        bewertungDS = Bewertung.objects.get(slug=bewertung)
        ds.name = name
        ds.kommentar = kommentar
        ds.bewertung = bewertungDS
        # DS Speichern
        ds.save()
        # Zur Liste zurückkehren
        return redirect("/")
    else:
        print("Da ist mächtig etwas schief gelaufen.")
    
def tgbNeu(request):
    if request.method == "GET":
        tabelleBewertung = Bewertung.objects.all().order_by("wert")
        template = 'app1/tgbneu.html'
        return render(request, template, {"tabbew":tabelleBewertung})
    else:
        name = request.POST['tgbname']
        kommentar = request.POST['tgbkommentar']
        bewertung = request.POST['tgbbewertung']
        button = request.POST['button']
        if button == "save":
            bewertungDS = Bewertung.objects.get(slug=bewertung)
            ds = Tagebuch(name=name, kommentar=kommentar, bewertung=bewertungDS)
            ds.save()
            template = 'app1/tgbdetail.html'
            return redirect("/")
        elif button == "cancel":
            return redirect("/")
        elif button == "delete":
            tabelleBewertung = Bewertung.objects.all().order_by("wert")
            template = 'app1/tgbneu.html'
            return render(request, template, {"tabbew":tabelleBewertung})

def kommineu(request):
    if request.method == "GET":
        tabelleBewertung = Bewertung.objects.all().order_by("wert")
        template = 'app1/bewertungeneu.html'
        return render(request, template, {"tabbew":tabelleBewertung})
    else:
        button = request.POST['button']
        if button == "save":
            slug = request.POST['bewertungname']
            beschreibung = request.POST['bkommentar']
            wert = int(request.POST['wert'])
            ds = Bewertung(slug=slug, beschreibung=beschreibung,wert=wert)
            ds.save()
            return redirect("/")
        elif button == "cancel":
            return redirect("/")
        elif button == "delete":
            tabelleBewertung = Bewertung.objects.all().order_by("wert")
            template = 'app1/bewertungeneu.html'
            return render(request, template, {"tabbew":tabelleBewertung})        

        