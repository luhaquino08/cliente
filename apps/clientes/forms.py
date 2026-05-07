from .models import Cliente
from django import forms

class ClienteForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    cpf = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    data_nascimento = forms.CharField(widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}))

    class Meta:
        model = Cliente
        fields = '__all__'