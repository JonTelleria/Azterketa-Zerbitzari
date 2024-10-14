from django.urls import path
from . import views

urlpatterns = [
     path('', views.paziente_list,name="base"),
    path('add-paziente/', views.add_paziente,name="add-paziente"),
    path('add-mediku/', views.add_mediku,name="add-mediku"),
    ]