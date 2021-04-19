from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import User
from .models import *
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
# Create your views here.

def cadastro(request):
    if request.method == 'POST':
        forms = FormConta(request.POST, request.FILES, instance=Conta(), prefix='')

        if forms.is_valid():
            conta = forms.save(commit=False)

            senha = conta.senha
            conta.senha = make_password(conta.senha)
            conta.conf_senha = conta.senha
            conta.save()
            user = User.objects.create_user(conta.cpf, conta.email, senha)
            nome = conta.nome.split()
            user.first_name = nome[0]
            user.save()
            messages.success(request, "Cadastro do "+conta.cpf+" realizado com sucesso.")
            return redirect('login')  

        messages.info(request, "Cadastro não realizado. ")
        context = {
            'form': forms
        }
        return render(request, 'registration/cadastro.html', context)

    forms = FormConta(instance=Conta(), prefix='')

    context = {
        'form': forms
    }
    return render(request, 'registration/cadastro.html', context)