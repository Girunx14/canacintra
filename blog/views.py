from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Categoria, Tag


def inicio(request):
    """Vista de página de inicio con las últimas publicaciones."""
    posts = Post.objects.filter(publicado=True)[:6]
    return render(request, 'blog/inicio.html', {'posts': posts})


def lista_posts(request):
    """Lista todas las publicaciones ordenadas por fecha."""
    posts = Post.objects.filter(publicado=True).select_related('autor', 'categoria')
    
    paginator = Paginator(posts, 9)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request, 'blog/lista_posts.html', {'posts': posts})


def detalle_post(request, slug):
    """Muestra el detalle de una publicación."""
    post = get_object_or_404(Post.objects.select_related('autor', 'categoria'), slug=slug, publicado=True)
    tags = post.tags.all()
    
    posts_relacionados = Post.objects.filter(
        categoria=post.categoria,
        publicado=True
    ).exclude(pk=post.pk)[:3]
    
    return render(request, 'blog/detalle_post.html', {
        'post': post,
        'tags': tags,
        'posts_relacionados': posts_relacionados
    })


def por_categoria(request, slug):
    """Filtra publicaciones por categoría."""
    categoria = get_object_or_404(Categoria, slug=slug)
    posts = Post.objects.filter(categoria=categoria, publicado=True).select_related('autor', 'categoria')
    
    paginator = Paginator(posts, 9)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request, 'blog/por_categoria.html', {
        'categoria': categoria,
        'posts': posts
    })


def por_tag(request, slug):
    """Filtra publicaciones por tag."""
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags=tag, publicado=True).select_related('autor', 'categoria')
    
    paginator = Paginator(posts, 9)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request, 'blog/por_tag.html', {
        'tag': tag,
        'posts': posts
    })
