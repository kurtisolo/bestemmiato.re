from django.shortcuts import render, redirect
from django.http import JsonResponse

from .forms import BestemmiaForm
from .models import BestemmiaBacheca

# questi servono per far andare l'audio
from django.conf import settings
import os
import uuid  # genera id univoco
from gtts import gTTS


def bacheca(request):
    bestemmie = BestemmiaBacheca.objects.order_by("-data_bestemmia")
    return render(request, "bacheca.html", {"bestemmie": bestemmie})


def crea_bestemmia(request):
    if request.method == "POST":
        form = BestemmiaForm(request.POST)
        if form.is_valid():
            bestemmia_bacheca = form.save()

            # Genera il file audio per la nuova bestemmia
            bestemmia_da_leggere = bestemmia_bacheca.bestemmia_bacheca
            tts = gTTS(text=bestemmia_da_leggere, lang="it")
            unique_id = str(uuid.uuid4())  # Genera un UUID univoco
            audio_file_name = f"audio_bacheca_{unique_id}.mp3"
            audio_file_path = os.path.join("static/audio_bacheca", audio_file_name)
            audio_file_full_path = os.path.join(settings.BASE_DIR, audio_file_path)
            tts.save(audio_file_full_path)
            bestemmia_bacheca.audio_file_path = audio_file_path
            bestemmia_bacheca.save()

            return redirect("bacheca")
    else:
        form = BestemmiaForm()
    return render(request, "crea_bestemmia.html", {"form": form})


def add_like(request, bestemmia_id):
    bestemmia_bacheca = BestemmiaBacheca.objects.get(id=bestemmia_id)
    bestemmia_bacheca.likes_bestemmia += 1
    bestemmia_bacheca.save()
    return redirect("bacheca")
