from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('noticias/', views.lista_posts, name='lista_posts'),
    path('noticia/<slug:slug>/', views.detalle_post, name='detalle_post'),
    path('categoria/<slug:slug>/', views.por_categoria, name='por_categoria'),
    path('tag/<slug:slug>/', views.por_tag, name='por_tag'),
    path('buscar/', views.buscar, name='buscar'),
    path('suscribir/', views.suscribir, name='suscribir'),
]
