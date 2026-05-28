# Explicação Detalhada: EcoStore

Este documento fornece uma visão técnica aprofundada sobre a arquitetura e as escolhas de implementação feitas no projeto EcoStore.

## 1. Arquitetura de Aplicações (Apps)

O Django segue o padrão "pluggable apps". Dividimos o projeto para garantir que cada parte tenha uma única responsabilidade:

### `core`
É o "coração" da interface. Aqui estão as views que não pertencem estritamente ao catálogo, como a `index` (home), `quem_somos` e `fale_conosco`. Também gerencia a autenticação estendendo as views nativas do Django (`LoginView`, `LogoutView`).

### `catalogo`
Gerencia o inventário. O modelo `Produto` possui uma `ForeignKey` para `Categoria`. Na view `listar_produtos`, utilizamos a biblioteca `requests` para consumir a `FakeStoreAPI`, demonstrando como integrar dados externos com dados locais.

### `vendas`
Foca na transação. Quando um usuário clica em "Comprar", a view `realizar_compra` executa uma **operação atômica**: cria um registro de `Pedido` e decrementa o campo `estoque` do `Produto`. Isso garante a integridade dos dados.

### `api_app`
Utiliza o **Django Rest Framework (DRF)**. Criamos `Serializers` que transformam objetos do banco de dados em JSON. Os `ViewSets` fornecem automaticamente os endpoints para listar, criar, atualizar e deletar (CRUD) via API.

## 2. Lógica de Negócio e Requisitos do PDF

### Fluxo de Compra e Estoque
A lógica implementada em `vendas/views.py` segue rigorosamente o pedido:
1. Verifica se o usuário está logado (`@login_required`).
2. Verifica se o `estoque > 0`.
3. Registra a venda e atualiza o estoque.
4. Redireciona para o perfil com uma mensagem de sucesso.

### Integração NoSQL/Firebase
A aplicação `feedback` está estruturada para usar o `firebase-admin`. Embora não tenhamos as chaves privadas reais do usuário para este novo projeto, o código segue o padrão corrigido anteriormente: uso de `firestore.client()` para persistência de avaliações fora do banco relacional.

### Interface Dinâmica (Templates)
No arquivo `templates/base.html`, usamos tags de template do Django (`{% if user.is_authenticated %}`) para alterar o menu. Se o usuário for `staff` (admin), ele vê o link para o Dashboard; se for cliente, vê o link para o Perfil.

## 3. Estrutura de Arquivos Principal

```text
ecostore_project/
├── ecostore/          # Configurações globais
│   ├── settings.py    # Apps instaladas, DB, Media/Static
│   └── urls.py        # Roteamento principal
├── core/              # Institucional e Auth
├── catalogo/          # Produtos e API Externa
├── vendas/            # Pedidos e Estoque
├── api_app/           # API REST (JSON)
├── templates/         # Arquivos HTML (Base e Apps)
├── static/            # CSS e Imagens
└── manage.py          # Utilitário de comando Django
```

## 4. Segurança e Boas Práticas
- **Proteção de Rotas:** Uso extensivo de decoradores para impedir acesso não autorizado.
- **Mensagens de Feedback:** Uso do `django.contrib.messages` para informar o usuário sobre o resultado de suas ações.
- **Upload de Mídia:** Configuração de `MEDIA_URL` e `MEDIA_ROOT` para gerenciar imagens de produtos corretamente.
