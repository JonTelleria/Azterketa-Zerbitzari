from django.urls import path
from . import views

urlpatterns = [
    
    path('add-paziente/', views.add_paziente,name="add-paziente"),
    path('add-mediku/', views.add_mediku,name="add-mediku"),
    ]