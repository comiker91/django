from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = 'app1/base.html'
    name = "Hans Dampf"
    return render(request,template,{'name':name,})