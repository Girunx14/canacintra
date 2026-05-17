from django import template
from blog.models import Categoria, Post

register = template.Library()


@register.simple_tag
def get_categories():
    """Retorna todas las categorías ordenadas alfabéticamente."""
    return Categoria.objects.all().order_by('nombre')


@register.simple_tag
def get_recent_posts(limit=5):
    """Retorna las publicaciones recientes."""
    return Post.objects.filter(publicado=True).order_by('-fecha_publicacion')[:limit]


@register.simple_tag
def get_related_posts(post, limit=3):
    """Retorna publicaciones relacionadas por categoría."""
    if post.categoria:
        return Post.objects.filter(
            categoria=post.categoria,
            publicado=True
        ).exclude(pk=post.pk)[:limit]
    return Post.objects.filter(publicado=True).exclude(pk=post.pk)[:limit]
