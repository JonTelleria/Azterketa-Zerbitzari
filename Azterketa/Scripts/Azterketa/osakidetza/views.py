from django.shortcuts import render, redirect
from .models import Paziente, Mediku, Zita
from .forms import PazienteForm, MedikuForm, ZitaForm
from django.http import HttpResponse
# Create your views here.
def paziente_list(request):
    pazienteZerrenda=Paziente.objects.all()
    return render(request, 'osakidetza/paziente_list.html', {'paziente': pazienteZerrenda})

def add_paziente(request):
    if request.method == 'POST':
        form = PazienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base') 
    else:
        form = PazienteForm()
        return render(request, 'osakidetza/add_paziente.html', {'formpaziente': form})
    
def add_mediku(request):
    if request.method == 'POST':
        form = MedikuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base') 
    else:
        form = MedikuForm()
        return render(request, 'osakidetza/add_mediku.html', {'formmediku': form})