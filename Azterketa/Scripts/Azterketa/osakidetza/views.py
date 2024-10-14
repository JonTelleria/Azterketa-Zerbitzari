from django.shortcuts import get_object_or_404, render, redirect
from .models import Paziente, Mediku, Zita
from .forms import PazienteForm, MedikuForm, ZitaForm, PazienteDeleteForm, MedikuDeleteForm
from django.http import HttpResponse
# Create your views here.
def zita_list(request):
    pazienteZerrenda=Zita.objects.all()
    return render(request, 'osakidetza/zita_list.html', {'zita': pazienteZerrenda})

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
    
def edit_paziente(request, id):
    paziente = Paziente.objects.filter(id=id)
    
    pazienteedit = Paziente.first()
    
    if not pazienteedit:
        return render(request, 'error.html', {'message': 'No se encontró paciente'})

    if request.method == 'POST':
        form = PazienteForm(request.POST, instance=pazienteedit)
        if form.is_valid():
            form.save()
            return redirect('default')  
    else:
        form = PazienteForm(instance=pazienteedit)

    return render(request, 'osakidetza/edit_paziente.html', {'formeditpaziente': form})

def edit_mediku(request, id):
    mediku = Paziente.objects.filter(id=id)
    
    medikuedit = Paziente.first()
    
    if not medikuedit:
        return render(request, 'error.html', {'message': 'No se encontró paciente'})

    if request.method == 'POST':
        form = MedikuForm(request.POST, instance=medikuedit)
        if form.is_valid():
            form.save()
            return redirect('default')  
    else:
        form = MedikuForm(instance=medikuedit)

    return render(request, 'osakidetza/edit_mediku.html', {'formeditmediku': form})

def delete_paziente(request):   
    if request.method == 'POST':
        form = PazienteDeleteForm(request.POST)  
        if form.is_valid(): 
            paziente = form.cleaned_data['paziente']  
            paziente.delete()  
            return redirect('paziente')     
    else:
        form = PazienteDeleteForm()  
        return render(request, 'osakidetza/delete_paziente.html', {'formdeletepaziente': form})
    
def delete_mediku(request):
   
    if request.method == 'POST':
        form = MedikuDeleteForm(request.POST)  
        if form.is_valid(): 
            mediku = form.cleaned_data['mediku']  
            mediku.delete()  
            return redirect('mediku')     
    else:
        form = MedikuDeleteForm()  
        return render(request, 'osakidetza/delete_mediku.html', {'formdeletemediku': form})
    
    
def zita_esleitu(request):
    if request.method == 'POST':
        form = ZitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base') 
    else:
        form = ZitaForm()
        return render(request, 'osakidetza/zita_esleitu.html', {'formzita': form})
    