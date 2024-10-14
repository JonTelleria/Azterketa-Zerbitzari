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
        fields=['pazientea','medikua','zita_data','oharra']
        
class PazienteDeleteForm(forms.ModelForm):
        class Meta:        
            model=Paziente
            fields=['paziente']  
        paziente = forms.ModelChoiceField(queryset=Paziente.objects.all(), label="Select Paziente")
        
class MedikuDeleteForm(forms.ModelForm):
        class Meta:        
            model=Mediku
            fields=['mediku']  
        mediku = forms.ModelChoiceField(queryset=Mediku.objects.all(), label="Select mediku")