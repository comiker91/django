from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tagebuchdetail/<int:comment_id>', views.tgbDetail, name='tgbdetails'),
    path('tagebuchdetail/neu/', views.tgbNeu, name='tgbneu'),
    path('bewertung/neu/', views.kommineu, name='kommentarneu'),
]