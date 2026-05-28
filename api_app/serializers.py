from rest_framework import serializers
from catalogo.models import Produto, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    categoria_nome = serializers.CharField(source='categoria.nome', read_only=True)

    class Meta:
        model = Produto
        fields = ['id', 'nome', 'descricao', 'preco', 'estoque', 'imagem', 'categoria', 'categoria_nome', 'data_criacao']
