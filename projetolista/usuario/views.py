from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Lista, ConteudoLista
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def cadastrar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        usuario = User.objects.filter(username=nome)

        if usuario:
            context = {
                'message': 'Já existe um usuario com esse nome'
            }
            return render(request, 'cadastrar.html', context)

        usuario = User.objects.create_user(username=nome, password=senha)

        usuario.save()
        return redirect('usuario:login')


    return render(request, 'cadastrar.html')

def logar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        usuario = authenticate(username=nome, password=senha)

        if usuario:
            login(request, usuario)
            return redirect('usuario:homepage')
        else:
            context = {
                'message': 'Nome ou senha incorretos'
            }
            return render(request, 'login.html', context)

    return render(request, 'login.html')

@login_required(login_url=('usuario:login'))
def homepage(request):
    listas = Lista.objects.filter(usuario=request.user).all()
    if request.method == 'POST':
        nome = request.POST.get('nome_lista')

        nome_existe = Lista.objects.filter(nome=nome)

        if nome_existe:
            context = {
                'listas': listas,
                'message': 'Já existe uma lista com esse nome'
            }
            return render(request, 'home.html', context)
        lista = Lista.objects.create(nome=nome, usuario=request.user)
        lista.save()
    context = {
        'listas': listas
    }
    return render(request, 'home.html', context)

def lista(request, lista_id):
    lista = get_object_or_404(Lista, id=lista_id)
    if request.method == 'POST':
        conteudo = request.POST.get('conteudo')
        criar_conteudo = ConteudoLista.objects.create(conteudo=conteudo, lista=lista)
        criar_conteudo.save()
    if lista.usuario != request.user:
        return HttpResponse('Essa lista possui a outro usuario')
    conteudos = ConteudoLista.objects.filter(lista=lista).all()
    context = {
        'lista': lista,
        'conteudos': conteudos
    }
    return render(request, 'lista.html', context)

# Create your views here.
