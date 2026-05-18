from django.contrib import admin
from .models import Categoria, Tag, Post, Comentario, Suscriptor, PostImagen


class PostImagenInline(admin.TabularInline):
    model = PostImagen
    extra = 3


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
    inlines = [PostImagenInline]
    list_display = [
        'titulo', 'autor', 'categoria', 'publicado', 
        'destacado', 'fecha_publicacion', 'get_comentarios_count'
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
    
    def get_comentarios_count(self, obj):
        return obj.get_comentarios_count()
    get_comentarios_count.short_description = 'Comentarios'


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['autor', 'post', 'aprobado', 'fecha_creacion']
    list_filter = ['aprobado', 'fecha_creacion']
    search_fields = ['contenido', 'autor__username', 'post__titulo']
    ordering = ['-fecha_creacion']
    
    actions = ['aprobar_seleccionados', 'desaprobar_seleccionados']
    
    def aprobar_seleccionados(self, request, queryset):
        queryset.update(aprobado=True)
        self.message_user(request, f'{queryset.count()} comentarios aprobados.')
    aprobar_seleccionados.short_description = 'Aprobar comentarios seleccionados'
    
    def desaprobar_seleccionados(self, request, queryset):
        queryset.update(aprobado=False)
        self.message_user(request, f'{queryset.count()} comentarios desaprobados.')
    desaprobar_seleccionados.short_description = 'Desaprobar comentarios seleccionados'


@admin.register(Suscriptor)
class SuscriptorAdmin(admin.ModelAdmin):
    list_display = ['email', 'fecha_registro', 'activo']
    list_filter = ['activo', 'fecha_registro']
    search_fields = ['email']
    ordering = ['-fecha_registro']

