from django import forms
from .models import Comentario


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
