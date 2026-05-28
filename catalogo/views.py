from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Categoria
import requests

def listar_produtos(request):
    produtos_locais = Produto.objects.all()
    produtos_api = []
    try:
        response = requests.get('https://fakestoreapi.com/products?limit=5', timeout=5)
        if response.status_code == 200:
            produtos_api = response.json()
    except:
        pass

    return render(request, 'catalogo/lista.html', {
        'produtos_locais': produtos_locais,
        'produtos_api': produtos_api
    })

def detalhe_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'catalogo/detalhe.html', {'produto': produto})
