from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from catalogo.models import Produto
from .models import Pedido

@login_required
def realizar_compra(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    if produto.estoque > 0:
        Pedido.objects.create(
            usuario=request.user,
            produto=produto,
            quantidade=1,
            valor_total=produto.preco
        )
        produto.estoque -= 1
        produto.save()
        messages.success(request, f'Compra de {produto.nome} realizada com sucesso!')
        return redirect('perfil')
    else:
        messages.error(request, 'Produto fora de estoque.')
        return redirect('lista_produtos')
