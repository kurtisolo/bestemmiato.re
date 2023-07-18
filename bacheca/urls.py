from django.urls import path
from . import views

urlpatterns = [
    path('', views.bacheca, name='bacheca'),
    path('contribuisci/', views.crea_bestemmia, name='crea_bestemmia'),
    path('liked/<int:bestemmia_id>/', views.add_like, name='add_like'),
]