from django import forms
from .models import Comentario, Post


class ComentarioForm(forms.ModelForm):
    """Formulario para crear comentarios."""
    
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Escribe tu comentario aquí...',
            })
        }
    
    def clean_contenido(self):
        contenido = self.cleaned_data.get('contenido')
        if len(contenido.strip()) < 10:
            raise forms.ValidationError('El comentario debe tener al menos 10 caracteres.')
        return contenido


class PostForm(forms.ModelForm):
    """Formulario para crear y editar publicaciones desde el frontend."""
    
    class Meta:
        model = Post
        fields = ['titulo', 'categoria', 'contenido', 'resumen', 'imagen_portada', 'publicado', 'destacado']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la noticia'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 8, 'placeholder': 'Escribe el cuerpo de la noticia aquí...'}),
            'resumen': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Breve resumen (se muestra en el carrusel y tarjetas)'}),
            'imagen_portada': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'publicado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'destacado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
