from django.urls import path
from . import views

app_name = 'usuario'
urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('login/', views.logar, name='login'),
    path('homepage/', views.homepage, name='homepage'),
    path('lista/<int:lista_id>', views.lista, name='lista')
]
