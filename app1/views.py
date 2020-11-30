from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = 'app1/base.html'
    tupel = ("Hans Dampf","Gut","lieber")
    return render(request,template,{'parameter':tupel})