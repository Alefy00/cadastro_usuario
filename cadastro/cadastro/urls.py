from django.urls import path
from usuario import views

urlpatterns = [
    path('',views.home, name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios')

]
