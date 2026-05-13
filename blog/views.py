from django.shortcuts import render
from .models import Post


def inicio(request):
    """Vista de página de inicio con las últimas publicaciones."""
    posts = Post.objects.filter(publicado=True)[:6]
    return render(request, 'blog/inicio.html', {'posts': posts})
