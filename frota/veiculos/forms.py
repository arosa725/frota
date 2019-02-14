from django.forms.widgets import ClearableFileInput
from django import forms
from .models import departamento,responsavel,veiculo,combustivel,posto,tabelacombustivel,manutencao, empresa, requisicao

class departamentoForm(forms.ModelForm):
    Nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    centrocusto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
          model = departamento
          fields = '__all__'
          widgets= {
                   'nome':forms.TextInput(attrs={
                   'class':'form-control', 
                   'maxlength': 255, 
                   'placeholder': 'Digite o Departamento'
                 })}

class responsavelForm(forms.ModelForm):
    cnh = forms.ImageField(widget=ClearableFileInput, required=False)
    aut = forms.ImageField(widget=ClearableFileInput, required=False)

    class Meta:
        model = responsavel
        fields = '__all__'
        widgets= {
                   'nome':forms.TextInput(attrs={
                   'class':'form-control', 
                   'maxlength': 255, 
                   'placeholder': 'Digite o nome do Usuário'
                 })}
                 
class veiculos(forms.ModelForm):
    class Meta:
          model = departamento
          fields = '__all__'