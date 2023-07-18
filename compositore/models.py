from django.db import models

"""
LEGENDA:
s = Spazio vuoto
_m = Maschile
_f = Femminile
_h = Hardcore
_s = Soft
_n = Nonsense
_crist = Cristiani
"""

class gods_crist_m(models.Model):
    parola = models.CharField(max_length=100)
    def __str__(self):
        return self.parola
    class Meta:
        verbose_name_plural = "Divinità maschili cristiane "

class insulti_h_m(models.Model):
    parola = models.CharField(max_length=100)
    def __str__(self):
        return self.parola
    class Meta:
        verbose_name_plural = "Insulti devastanti"

class insulti_s_m(models.Model):
    parola = models.CharField(max_length=100)
    def __str__(self):
        return self.parola
    class Meta:
        verbose_name_plural = "Insulti delicati"

class insulti_n_m(models.Model):
    parola = models.CharField(max_length=100)
    def __str__(self):
        return self.parola
    class Meta:
        verbose_name_plural = "Insulti medi"