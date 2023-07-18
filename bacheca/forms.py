from django import forms
from .models import BestemmiaBacheca

class BestemmiaForm(forms.ModelForm):
    class Meta:
        model = BestemmiaBacheca
        fields = ['bestemmia_bacheca']