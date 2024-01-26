from django.contrib import admin
from django.urls import path
from . import views
from .views import *
urlpatterns = [
    #path('', indexPage,name='list'),  
    path('', views.indexPage,name='inicio'),
   path('api/contenido_menu/', ContenidoMenuListCreateView.as_view(), name='contenido_menu-list-create'),
    path('api/contenido_menu/<int:pk>/', ContenidoMenuDetailView.as_view(), name='contenido_menu-detail'),

]