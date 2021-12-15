from django import forms
from django.forms.widgets import ClearableFileInput
from .models import Chamado, Setor

class ChamadoForm(forms.ModelForm):
    foto = forms.ImageField(widget=ClearableFileInput, required=False)


    class Meta:
        model = Chamado
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 100, 'required': False}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'maxlength': 255, 'required': False}),
        }

class SetorForm(forms.ModelForm):

    class Meta:
        model = Setor
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 100}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 100, 'required': False}),
        }