from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Categoria(models.Model):
    """Categorías para clasificar las publicaciones del blog."""
    nombre = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre


class Tag(models.Model):
    """Etiquetas para las publicaciones del blog."""
    nombre = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    class Meta:
        ordering = ['nombre']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre


class Post(models.Model):
    """Publicaciones del blog."""
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    contenido = models.TextField()
    autor = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='posts'
    )
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='posts'
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    imagen_portada = models.ImageField(
        upload_to='posts/%Y/%m/', 
        blank=True, 
        null=True
    )
    resumen = models.TextField(
        blank=True, 
        help_text='Resumen corto de la publicación (opcional)'
    )
    publicado = models.BooleanField(default=False)
    destacado = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    fecha_publicacion = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-fecha_publicacion', '-fecha_creacion']
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        indexes = [
            models.Index(fields=['-fecha_publicacion']),
            models.Index(fields=['publicado']),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    def get_resumen(self):
        if self.resumen:
            return self.resumen
        return self.contenido[:150] + '...'
    
    def get_comentarios_count(self):
        """Retorna la cantidad de comentarios aprobados."""
        return self.comentarios.filter(aprobado=True).count()


class Comentario(models.Model):
    """Comentarios de los usuarios en las publicaciones."""
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE, 
        related_name='comentarios'
    )
    autor = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='comentarios'
    )
    contenido = models.TextField(help_text='Tu comentario')
    aprobado = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['fecha_creacion']
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        indexes = [
            models.Index(fields=['aprobado']),
            models.Index(fields=['fecha_creacion']),
        ]

    def __str__(self):
        return f'Comentario de {self.autor.username} en {self.post.titulo}'
