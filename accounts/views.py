from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


def registro(request):
    """Vista para registro de nuevos usuarios."""
    if request.user.is_authenticated:
        return redirect('blog:inicio')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Cuenta creada exitosamente!')
            return redirect('blog:inicio')
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/registro.html', {'form': form})


def login_usuario(request):
    """Vista para inicio de sesión de usuarios."""
    if request.user.is_authenticated:
        return redirect('blog:inicio')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'¡Bienvenido {username}!')
                return redirect('blog:inicio')
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout_usuario(request):
    """Vista para cerrar sesión."""
    logout(request)
    messages.info(request, 'Has cerrado sesión correctamente.')
    return redirect('blog:inicio')


@login_required
def perfil(request):
    """Vista para ver el perfil del usuario autenticado."""
    return render(request, 'accounts/perfil.html', {'user': request.user})
