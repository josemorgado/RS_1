from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('puntuaciones_usuario/',views.mostrar_puntuaciones_usuario),
    path('peliculas_similares/',views.mostrar_peliculas_parecidas),
    path('recomendar_peliculas_usuarios/',views.recomendar_peliculas_usuario_RSusuario),
    path('',views.index),
    path('index.html/', views.index),
    path('populate/', views.populateDatabase),
    path('loadRS/', views.loadRS),
    path('ingresar/', views.ingresar),    
    path('admin/',admin.site.urls),
    ]
