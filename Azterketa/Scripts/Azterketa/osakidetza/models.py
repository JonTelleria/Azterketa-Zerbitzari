from django.db import models
from django.utils import timezone
# Create your models here.

class Paziente(models.Model):
    id = models.AutoField(primary_key=True)
    izena = models.CharField(max_length=75)
    abizena = models.CharField(max_length=100)
    jaiotze_data = models.DateTimeField(default=timezone.now)
    emaila = models.CharField(max_length=100)
    mugikorra = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.izena} {self.abizena} "
    
class Mediku(models.Model):
    id = models.AutoField(primary_key=True)
    izena = models.CharField(max_length=75)
    abizena = models.CharField(max_length=100)
    espezializazioa = models.CharField(max_length=100)
    
    def __str__(self):
        return f" {self.izena} {self.abizena} {self.espezializazioa}."
    
class Zita(models.Model):
    zita_data = models.DateTimeField(default=timezone.now)
    oharra = models.CharField(max_length=100)
    pazientea = models.ForeignKey(Paziente, to_field='id', on_delete=models.CASCADE)
    medikua = models.ForeignKey(Mediku, to_field='id', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.pazientea}-k {self.medikua} medikuarekin {self.zita_data} egunenan zita dauka. Gogoratu : {self.oharra} ."