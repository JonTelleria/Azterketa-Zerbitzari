from django import forms 
from .models import Paziente, Mediku, Zita

class PazienteForm(forms.ModelForm):    
    class Meta:        
        model=Paziente        
        fields=['izena','abizena','jaiotze_data','emaila','mugikorra']


class MedikuForm(forms.ModelForm):    
    class Meta:        
        model=Mediku        
        fields=['izena','abizena','espezializazioa']
        
        
class ZitaForm(forms.ModelForm):    
    class Meta:        
        model=Zita        
        fields=['zita_data','oharra','pazientea','medikua']