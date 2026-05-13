from django.contrib import admin
from .models import Categoria, Tag, Post


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug', 'descripcion']
    prepopulated_fields = {'slug': ('nombre',)}
    search_fields = ['nombre', 'descripcion']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug']
    prepopulated_fields = {'slug': ('nombre',)}
    search_fields = ['nombre']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'titulo', 'autor', 'categoria', 'publicado',
        'destacado', 'fecha_publicacion'
    ]
    list_filter = ['publicado', 'destacado', 'categoria', 'fecha_publicacion']
    search_fields = ['titulo', 'contenido', 'resumen']
    prepopulated_fields = {'slug': ('titulo',)}
    raw_id_fields = ['autor']
    date_hierarchy = 'fecha_publicacion'
    ordering = ['-fecha_publicacion']
    filter_horizontal = ['tags']

    fieldsets = (
        ('Información principal', {
            'fields': ('titulo', 'slug', 'autor', 'categoria')
        }),
        ('Contenido', {
            'fields': ('contenido', 'resumen', 'imagen_portada')
        }),
        ('Estado', {
            'fields': ('publicado', 'destacado', 'fecha_publicacion')
        }),
        ('Etiquetas', {
            'fields': ('tags',)
        }),
    )
