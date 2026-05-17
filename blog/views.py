from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import re
from .models import Post, Categoria, Tag, Comentario, Suscriptor
from .forms import ComentarioForm


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
    comentarios = post.comentarios.filter(aprobado=True).select_related('autor')
    
    posts_relacionados = Post.objects.filter(
        categoria=post.categoria,
        publicado=True
    ).exclude(pk=post.pk)[:3]
    
    # Formulario de comentario
    form = None
    if request.user.is_authenticated:
        form = ComentarioForm()
        if request.method == 'POST':
            form = ComentarioForm(request.POST)
            if form.is_valid():
                comentario = form.save(commit=False)
                comentario.post = post
                comentario.autor = request.user
                comentario.save()
                messages.success(request, 'Tu comentario se envió correctamente. Será revisado por un moderador.')
                return redirect('blog:detalle_post', slug=post.slug)
    
    return render(request, 'blog/detalle_post.html', {
        'post': post,
        'tags': tags,
        'posts_relacionados': posts_relacionados,
        'comentarios': comentarios,
        'form': form,
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


def buscar(request):
    """Busca publicaciones por término."""
    query = request.GET.get('q', '')
    posts = Post.objects.filter(publicado=True).select_related('autor', 'categoria')
    
    if query:
        posts = posts.filter(
            Q(titulo__icontains=query) |
            Q(contenido__icontains=query) |
            Q(resumen__icontains=query)
        )
    
    paginator = Paginator(posts, 9)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request, 'blog/buscar.html', {
        'posts': posts,
        'query': query
    })


@require_POST
def suscribir(request):
    """Registra una nueva suscripción por correo electrónico vía AJAX."""
    email = request.POST.get('email', '').strip()
    
    if not email:
        return JsonResponse({
            'status': 'error',
            'message': 'Por favor, introduce una dirección de correo electrónico.'
        }, status=400)
    
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        return JsonResponse({
            'status': 'error',
            'message': 'El formato de correo electrónico no es válido.'
        }, status=400)
        
    try:
        suscriptor, creado = Suscriptor.objects.get_or_create(email=email)
        if creado:
            return JsonResponse({
                'status': 'success',
                'message': '¡Gracias por suscribirte a nuestro boletín de noticias!'
            })
        else:
            if not suscriptor.activo:
                suscriptor.activo = True
                suscriptor.save()
                return JsonResponse({
                    'status': 'success',
                    'message': '¡Tu suscripción ha sido reactivada con éxito!'
                })
            return JsonResponse({
                'status': 'info',
                'message': 'Esta dirección de correo electrónico ya está suscrita.'
            })
    except Exception:
        return JsonResponse({
            'status': 'error',
            'message': 'Hubo un error al procesar tu solicitud. Por favor, intenta de nuevo.'
        }, status=500)


