from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log in the user after successful registration
            login(request, user)
            return redirect('home')  # Redirige a la página de inicio después del registro
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/register.html', {'form': form})


from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'main/login.html'
    success_url = '/home/'  # Redirige a la página de inicio después del login



@login_required
def home(request):
    return render(request, 'main/home.html')

from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    next_page = 'login'  # Redirige a la página de inicio de sesión después de cerrar sesión

