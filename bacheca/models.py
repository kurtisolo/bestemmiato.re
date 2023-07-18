from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class BestemmiaBacheca(models.Model):
    bestemmia_bacheca = models.CharField(max_length=500)
    data_bestemmia = models.DateTimeField(default=datetime.now)
    likes_bestemmia = models.IntegerField(default=0)
    audio_file_path = models.CharField(max_length=255, blank=True)
    autore = models.CharField(max_length=100, default='Anonimo')
    def __str__(self):
        return self.bestemmia_bacheca
    class Meta:
        verbose_name_plural = "Bestemmie bacheca"