from django import forms 
from .models import Paziente, Mediku, Zita

class PazienteForm(forms.ModelForm):    
    class Meta:        
        model=Paziente        
        fields=['izena','abizena','jaiotze_data','emaila','mugikorra']


class PertsonaForm(forms.ModelForm):    
    class Meta:        
        model=Mediku        
        fields=['izena','abizena','espezializazioa']
        
        
class PertsonaForm(forms.ModelForm):    
    class Meta:        
        model=Mediku        
        fields=['zita_data','oharra','pazientea','medikua']