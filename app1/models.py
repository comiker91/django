from django.db import models

# Create your models here.

class Tagebuch(models.Model):
    name = models.CharField(max_length=50)
    zeitpunkt = models.DateTimeField(auto_now=False, auto_now_add=True)
    kommentar = models.TextField()
    bewertung = models.IntegerField()