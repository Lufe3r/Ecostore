from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quem-somos/', views.quem_somos, name='quem_somos'),
    path('fale-conosco/', views.fale_conosco, name='fale_conosco'),
    path('perfil/', views.perfil, name='perfil'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('alterar-senha/', views.alterar_senha, name='alterar_senha'),
    path('produtos-admin/', views.produtos_admin, name='produtos_admin'),
    path('categorias/', views.categorias, name='categorias'),
    path('compras/', views.compras, name='compras'),
    path('contatos-admin/', views.contatos_admin, name='contatos_admin'),
    path('avaliacoes/', views.avaliacoes, name='avaliacoes'),
    path('usuarios/', views.usuarios_admin, name='usuarios_admin'),
    path('usuarios/excluir/<int:id>/', views.excluir_usuario, name='excluir_usuario'),
    path('produtos-admin/', views.produtos_admin, name='produtos_admin'),
    path('produtos/excluir/<int:id>/', views.excluir_produto, name='excluir_produto'),
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/excluir/<int:id>/', views.excluir_categoria, name='excluir_categoria'),
    path('compras/', views.compras, name='compras'),
    path('compras/excluir/<int:id>/', views.excluir_compra, name='excluir_compra'),
    path('contatos/', views.contatos_admin, name='contatos_admin'),
    path('contatos/excluir/<int:id>/', views.excluir_contato, name='excluir_contato'),
    path('avaliacoes/', views.avaliacoes, name='avaliacoes'),
    path('avaliacoes/excluir/<int:id>/', views.excluir_avaliacao, name='excluir_avaliacao'),
    # PRODUTOS

path(
    'produto/adicionar/',
    views.adicionar_produto,
    name='adicionar_produto'
),

path(
    'produto/editar/<int:id>/',
    views.editar_produto,
    name='editar_produto'
),

path(
    'produto/excluir/<int:id>/',
    views.excluir_produto,
    name='excluir_produto'
),

# CATEGORIAS

path(
    'categoria/adicionar/',
    views.adicionar_categoria,
    name='adicionar_categoria'
),

path(
    'categoria/editar/<int:id>/',
    views.editar_categoria,
    name='editar_categoria'
),

path(
    'categoria/excluir/<int:id>/',
    views.excluir_categoria,
    name='excluir_categoria'
),
# USUÁRIOS
path('usuarios/', views.usuarios_admin, name='usuarios_admin'),
path('usuarios/excluir/<int:id>/', views.excluir_usuario, name='excluir_usuario'),
]
