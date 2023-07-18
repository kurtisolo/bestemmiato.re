from django import forms

class MyForm(forms.Form):
    POTENZA = [('', '---------'), ('leggera', 'Leggera'), ('media', 'Media'), ('devastante', 'Devastante')]
    COMPLESS = [('', '---------'), ('semplice', 'Semplice'), ('elaborata', 'Elaborato'), ('molto elaborata', 'Molto elaborato')]

    potenza = forms.ChoiceField(choices=POTENZA, required=True)
    complessita = forms.ChoiceField(choices=COMPLESS, required=True)