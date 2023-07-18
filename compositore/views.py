from django.shortcuts import render
from .forms import MyForm
from .models import gods_crist_m, insulti_h_m, insulti_s_m, insulti_n_m

# questi servono per far andare l'audio
from django.conf import settings
import os
import uuid #genera id univoco
import random
from gtts import gTTS

s = " "

def bestemmia(tipo_insulto, form, complessita):
    
    gods_crist_mx = gods_crist_m.objects.values_list('parola', flat=True)
    
    if complessita == "semplice":
        divinità = random.choice(gods_crist_mx)
        insulto = random.choice(tipo_insulto)
        risultato = f"{divinità}{s}{insulto}"

    elif complessita == "elaborata":
        divinità = random.choice(gods_crist_mx)
        insulto = random.choice(tipo_insulto)
        insulto2 = random.choice(tipo_insulto)
        if insulto == insulto2:
            insulto2 = random.choice(tipo_insulto)
        risultato = f"{divinità}{s}{insulto}{s}{insulto2}"
    
    elif complessita == "molto elaborata":
        divinità = random.choice(gods_crist_mx)
        insulto2 = insulto3 = insulto4 = ""
        insulto = random.choice([i for i in tipo_insulto if i != insulto2 and i != insulto3 and i != insulto4])
        insulto2 = random.choice([i for i in tipo_insulto if i != insulto and i != insulto3 and i != insulto4])
        insulto3 = random.choice([i for i in tipo_insulto if i != insulto and i != insulto2 and i != insulto4])
        insulto4 = random.choice([i for i in tipo_insulto if i != insulto and i != insulto2 and i != insulto3])
        risultato = f"{divinità}{s}{insulto}{s}{insulto2}{s}{insulto3}{s}e{s}{insulto4}"
    
    text = risultato
    tts = gTTS(text=text, lang='it')
    unique_id = str(uuid.uuid4())  # Genera un UUID univoco
    audio_file_name = f"audio_{unique_id}.mp3"
    audio_file_path = os.path.join("static", audio_file_name)
    audio_file_full_path = os.path.join(settings.BASE_DIR, audio_file_path)
    tts.save(audio_file_full_path)
    def delete_previous_audio_files(directory, current_file_name):
        for filename in os.listdir(directory):
            if filename != current_file_name and filename.startswith("audio_") and filename.endswith(".mp3"):
                file_path = os.path.join(directory, filename)
                os.remove(file_path)
    delete_previous_audio_files("static", audio_file_name)

    return risultato, audio_file_path

def home(request):

    insulti_h_mx = insulti_h_m.objects.values_list('parola', flat=True)
    insulti_n_mx = insulti_n_m.objects.values_list('parola', flat=True)
    insulti_s_mx = insulti_s_m.objects.values_list('parola', flat=True)

    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            potenza = form.cleaned_data['potenza']
            complessita = form.cleaned_data['complessita']
            if potenza == "devastante":
                risultato, audio_file_path = bestemmia(insulti_h_mx, form, complessita)
            elif potenza == "media":
                risultato, audio_file_path = bestemmia(insulti_n_mx, form, complessita)
            elif potenza == "leggera":
                risultato, audio_file_path = bestemmia(insulti_s_mx, form, complessita)
            return render(request, 'risultato.html', {'risultato': risultato, 'potenza': potenza, 'complessita': complessita, 'form': form, 'audio_file_path': audio_file_path})
    else:
        form = MyForm()
    return render(request, 'inserire_dati.html', {'form': form})

