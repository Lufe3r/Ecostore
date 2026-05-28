from django.db import models
from django.contrib.auth.models import User
from catalogo.models import Produto

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pedidos')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.usuario.username}"
