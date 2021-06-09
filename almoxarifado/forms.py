from django.forms import ModelForm
from almoxarifado.models import Produtos

class RegistroProdutos(ModelForm):
    class Meta:
        model = Produtos
        fields = ['id', 'nome', 'quantidade', 'data']

