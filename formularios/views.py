from django.shortcuts import render
from django.http import HttpResponse
from formularios.forms import formularioCadastro


def home(request): #renderizo o meu formulário HTML
    return render(request, 'formularios/home.html')

def home_forms(request): #renderizo o meu formulário FORMS
    form = formularioCadastro()
    return render(request, 'formularios/home_forms.html', {'form': form})

def processa_formulario(request): #associado ao template home
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    return HttpResponse(f'{nome} {email}')

def processa_formulario_forms(request):
    form = formularioCadastro(request.POST)
    if form.is_valid():
        nome = form.data['nome']
        email = form.data['email']
        return HttpResponse(f'{nome} {email}')
    return HttpResponse('erro interno do sistema')