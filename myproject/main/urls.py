from django.urls import path
from . import views

urlpatterns = [
    path('', views.CustomLoginView.as_view(), name='login'),  # Ruta para la página de inicio de sesión
    path('home/', views.home, name='home'),  # Ruta para la página de inicio
    path('register/', views.register, name='register'),  # Ruta para la página de registro
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),  # Ruta para cerrar sesión
]
