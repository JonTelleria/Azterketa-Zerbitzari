from django.urls import path
from . import views

urlpatterns = [
     path('', views.zita_list,name="base"),
    path('add-paziente/', views.add_paziente,name="add-paziente"),
    path('add-mediku/', views.add_mediku,name="add-mediku"),
    path('edit-paziente/<str:izena>/', views.edit_paziente,name="edit-paziente"),
    path('delete-paziente/', views.delete_paziente,name="delete-paziente"),
    path('delete-mediku/', views.delete_mediku,name="delete-mediku"),
    path('zita-esleitu/', views.zita_esleitu,name="zita-esleitu"),
    ]