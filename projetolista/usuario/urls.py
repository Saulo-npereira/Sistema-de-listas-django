from django.urls import path
from . import views

app_name = 'usuario'
urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('login/', views.logar, name='login'),
    path('homepage/', views.homepage, name='homepage'),
    path('lista/<int:lista_id>', views.lista, name='lista'),
    path('deletar_lista/<int:id_lista>', views.deletar_lista, name='deletar_lista'),
    path('deletar_conteudo/<int:id_conteudo>', views.deletar_conteudo, name='deletar_conteudo'),
]
