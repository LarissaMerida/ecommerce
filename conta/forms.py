from django import forms
from .models import *

class FormConta(forms.ModelForm):
    nome= forms.CharField(label = 'Nome', max_length = 255, widget = forms.TextInput(attrs = {'class':'form-control required', 'placeholder': 'Nome'}))
    cpf= forms.CharField(label = 'CPF', max_length = 255, widget = forms.TextInput(attrs = {'class':'form-control required', 'placeholder': 'CPF'}))
    endereco= forms.CharField(label = 'Endereço', max_length = 255, widget = forms.TextInput(attrs = {'class':'form-control required',  'placeholder': 'Endereço'}))
    email= forms.CharField(label = 'E-mail', max_length = 255, widget = forms.EmailInput(attrs = {'class':'form-control required',  'placeholder': 'E-mail'}))
    senha = forms.CharField(label = 'Senha', max_length = 255, widget = forms.PasswordInput(attrs = {'class':'form-control required'}))
    conf_senha= forms.CharField(label = 'Confirme a senha', max_length = 255, widget = forms.PasswordInput(attrs = {'class':'form-control required'}))
    


    class Meta:
        model = Conta
        fields = ['nome', 'endereco', 'cpf', 'email', 'senha', 'conf_senha']
