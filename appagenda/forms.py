from django import forms 
from .models import Cidadao


class CidadaoForm(forms.ModelForm):
    class Meta: 
        model = Cidadao
        fields = ['nome', 'cpf', 'email', 'data_nascimento', 'celular', 'cep', 'endereco', 'endereco_numero']
        labels = {
        'nome': 'Nome do Cidadão'
    }
    widgets = {
        'nome': forms.TextInput(attrs={'class':'form-control'}),
        'cpf': forms.TextInput(attrs={'class':'form-control'}),
 
    }