from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from almoxarifado.models import Produtos
from almoxarifado.forms import RegistroProdutos

# Create your views here.

'''def homeView(request):
    return render()'''

def createView(request):
    form = RegistroProdutos(request.POST)
    if form.is_valid():
        form.save()
        return redirect("lista")
    return render(request, 'create.html', {'form': form})

def readView(request):
    nome = Produtos.objects.all()
    return render(request, 'read.html', {'nome': nome})

def updateView(request, id):
    nome = get_object_or_404(Produtos, pk=id)
    form = RegistroProdutos(request.POST or None, instance=nome)
    if form.is_valid():
        form.save()
        return redirect('lista')
    return render(request, 'update.html', {'form': form})

def deleteView(request, id):
     cadeira = get_object_or_404(Produtos, pk=id)
     if request.method == 'POST':
         cadeira.delete()
         return redirect('lista')
     return render(request, 'delete.html',{'cadeira':cadeira})







