from django.db import models
from django.db.models.fields import IntegerField
from django.db.models.lookups import Exact

# Create your models here.

class Tagebuch(models.Model):
    name = models.CharField(max_length=50)
    zeitpunkt = models.DateTimeField(auto_now=False, auto_now_add=True)
    kommentar = models.TextField()
    bewertung = models.IntegerField()
    def __str__(self):
        return self.name+", ("+str(self.bewertung)+"), "+self.kommentar
    class Meta:
        verbose_name_plural = "Tagebuch"

class Bewertung(models.Model):
    slug = models.CharField(max_length=10, unique=True)
    beschreibung = models.CharField(max_length=50)
    wert = models.IntegerField()
    def __str__(self):
        return "("+str(self.wert)+") "+self.slug
    class Meta:
        verbose_name_plural = "Bewertung"