from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import ProdutoForm, CategoriaForm
from .models import Contato, Avaliacao
from catalogo.models import Produto, Categoria
from vendas.models import Pedido


# =========================
# PÁGINAS PÚBLICAS
# =========================
@login_required
def produtos_admin(request):

    if not request.user.is_staff:
        return redirect('index')

    produtos = Produto.objects.all()

    return render(request, 'core/produtos.html', {
        'produtos': produtos
    })

def index(request):
    produtos_destaque = Produto.objects.all()[:3]

    avaliacoes = [
        {
            'cliente': 'Maria Silva',
            'comentario': 'Produtos incríveis e entrega rápida!',
            'nota': 5
        },
        {
            'cliente': 'João Pereira',
            'comentario': 'Adorei a iniciativa sustentável.',
            'nota': 4
        },
    ]

    return render(request, 'core/index.html', {
        'produtos': produtos_destaque,
        'avaliacoes': avaliacoes
    })


def quem_somos(request):

    desenvolvedores = [
        {
            'nome': 'Luiz Felipe Fernandes de Mello',
            'cargo': 'Desenvolvedor Back-End'
        },
        {
            'nome': 'Vinicius Gomes',
            'cargo': 'Desenvolvedor Front-End'
        },
    ]

    return render(request, 'core/quem_somos.html', {
        'desenvolvedores': desenvolvedores
    })


def fale_conosco(request):

    if request.method == 'POST':

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        assunto = request.POST.get('assunto')
        mensagem = request.POST.get('mensagem')

        Contato.objects.create(
            nome=nome,
            email=email,
            assunto=assunto,
            mensagem=mensagem
        )

        messages.success(request, 'Mensagem enviada com sucesso!')

        return redirect('index')

    return render(request, 'core/fale_conosco.html')


def cadastrar(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('index')

    else:
        form = UserCreationForm()

    return render(request, 'registration/cadastrar.html', {
        'form': form
    })


# =========================
# PERFIL
# =========================

@login_required
def perfil(request):

    pedidos = Pedido.objects.filter(
        usuario=request.user
    ).order_by('-data_pedido')

    return render(request, 'core/perfil.html', {
        'pedidos': pedidos
    })


@login_required
def alterar_senha(request):

    if request.method == 'POST':

        form = PasswordChangeForm(
            request.user,
            request.POST
        )

        if form.is_valid():

            user = form.save()

            update_session_auth_hash(request, user)

            messages.success(
                request,
                'Senha alterada com sucesso!'
            )

            return redirect('perfil')

    else:

        form = PasswordChangeForm(request.user)

    return render(request, 'registration/alterar_senha.html', {
        'form': form
    })


# =========================
# DASHBOARD ADMIN
# =========================

@login_required
def dashboard(request):

    if not request.user.is_staff:
        return redirect('index')

    stats = {
        'usuarios': User.objects.count(),
        'produtos': Produto.objects.count(),
        'categorias': Categoria.objects.count(),
        'vendas': Pedido.objects.count(),
        'contatos': Contato.objects.count(),
        'avaliacoes': Avaliacao.objects.count(),
    }

    return render(request, 'core/dashboard.html', {
        'stats': stats
    })


# =========================
# USUÁRIOS
# =========================

@login_required
def adicionar_produto(request):

    if not request.user.is_staff:
        return redirect('index')

    form = ProdutoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('produtos_admin')

    return render(request, 'core/form.html', {
        'form': form,
        'titulo': 'Adicionar Produto'
    })


@login_required
def editar_produto(request, id):

    if not request.user.is_staff:
        return redirect('index')

    produto = Produto.objects.get(id=id)

    form = ProdutoForm(
        request.POST or None,
        request.FILES or None,
        instance=produto
    )

    if form.is_valid():
        form.save()
        return redirect('produtos_admin')

    return render(request, 'core/form.html', {
        'form': form,
        'titulo': 'Editar Produto'
    })


@login_required
def excluir_produto(request, id):

    if not request.user.is_staff:
        return redirect('index')

    produto = Produto.objects.get(id=id)

    if request.method == 'POST':
        produto.delete()
        return redirect('produtos_admin')

    return render(request, 'core/confirmar_exclusao.html', {
        'objeto': produto,
        'voltar': '/produtos-admin/'
    })


# =========================
# CATEGORIAS
# =========================

@login_required
def categorias(request):

    if not request.user.is_staff:
        return redirect('index')

    categorias = Categoria.objects.all()

    return render(request, 'core/categorias.html', {
        'categorias': categorias
    })

@login_required
def adicionar_categoria(request):

    if not request.user.is_staff:
        return redirect('index')

    form = CategoriaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('categorias')

    return render(request, 'core/form.html', {
        'form': form,
        'titulo': 'Adicionar Categoria'
    })


@login_required
def editar_categoria(request, id):

    if not request.user.is_staff:
        return redirect('index')

    categoria = Categoria.objects.get(id=id)

    form = CategoriaForm(
        request.POST or None,
        instance=categoria
    )

    if form.is_valid():
        form.save()
        return redirect('categorias')

    return render(request, 'core/form.html', {
        'form': form,
        'titulo': 'Editar Categoria'
    })


@login_required
def excluir_categoria(request, id):

    if not request.user.is_staff:
        return redirect('index')

    categoria = Categoria.objects.get(id=id)

    if request.method == 'POST':
        categoria.delete()
        return redirect('categorias')

    return render(request, 'core/confirmar_exclusao.html', {
        'objeto': categoria,
        'voltar': '/categorias/'
    })


# =========================
# COMPRAS
# =========================

@login_required
def compras(request):

    if not request.user.is_staff:
        return redirect('index')

    compras = Pedido.objects.all().order_by('-data_pedido')

    return render(request, 'core/compras.html', {
        'compras': compras
    })


@login_required
def excluir_compra(request, id):

    if not request.user.is_staff:
        return redirect('index')

    compra = get_object_or_404(Pedido, id=id)

    compra.delete()

    return redirect('compras')


# =========================
# CONTATOS
# =========================

@login_required
def contatos_admin(request):

    if not request.user.is_staff:
        return redirect('index')

    contatos = Contato.objects.all().order_by('-id')

    return render(request, 'core/contatos.html', {
        'contatos': contatos
    })


@login_required
def excluir_contato(request, id):

    if not request.user.is_staff:
        return redirect('index')

    contato = get_object_or_404(Contato, id=id)

    contato.delete()

    return redirect('contatos_admin')


# =========================
# AVALIAÇÕES
# =========================

@login_required
def avaliacoes(request):

    if not request.user.is_staff:
        return redirect('index')

    avaliacoes = Avaliacao.objects.all().order_by('-id')

    return render(request, 'core/avaliacoes.html', {
        'avaliacoes': avaliacoes
    })


@login_required
def excluir_avaliacao(request, id):

    if not request.user.is_staff:
        return redirect('index')

    avaliacao = get_object_or_404(Avaliacao, id=id)

    avaliacao.delete()

    return redirect('avaliacoes')

# =========================
# USUÁRIOS ADMIN
# =========================

@login_required
def usuarios_admin(request):

    if not request.user.is_staff:
        return redirect('index')

    usuarios = User.objects.all().order_by('-date_joined')

    return render(request, 'core/usuarios.html', {
        'usuarios': usuarios
    })


@login_required
def excluir_usuario(request, id):

    if not request.user.is_staff:
        return redirect('index')

    usuario = User.objects.get(id=id)

    if usuario != request.user:
        usuario.delete()

    return redirect('usuarios_admin')