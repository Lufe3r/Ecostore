# EcoStore - Loja de Produtos Sustentáveis 🌿

Este é um projeto de e-commerce desenvolvido em Django, baseado nos requisitos de um projeto final de Web 3. A EcoStore foca na venda de produtos ecológicos e sustentáveis, integrando tecnologias modernas como Firebase e APIs externas.

## 🚀 Funcionalidades Principais

### Para Clientes:
- **Catálogo de Produtos:** Visualização de produtos locais e integração em tempo real com a `FakeStoreAPI`.
- **Sistema de Compras:** Usuários logados podem realizar compras, com atualização automática de estoque.
- **Perfil do Usuário:** Histórico completo de pedidos e dados cadastrais.
- **Autenticação Completa:** Cadastro, Login, Logout e Alteração de Senha.
- **Feedback:** Sistema de avaliações integrado (preparado para NoSQL/Firebase).

### Para Administradores:
- **Dashboard Estatístico:** Visão geral de usuários, produtos, vendas e contatos.
- **CRUD Completo via Django Admin:** Gerenciamento total de categorias, produtos e pedidos.
- **Gestão de Contatos:** Visualização de mensagens enviadas pelos clientes.

## 🛠️ Estrutura do Código

O projeto está dividido em aplicações modulares para facilitar a manutenção:

- **`ecostore/`**: Configurações centrais do projeto (settings, urls globais).
- **`core/`**: Gerencia a interface institucional, autenticação e perfil do usuário.
- **`catalogo/`**: Responsável pelos modelos de `Produto` e `Categoria`, além da integração com APIs externas.
- **`vendas/`**: Lógica de processamento de pedidos e controle de estoque.
- **`feedback/`**: Estrutura para avaliações e integração com Firebase.
- **`api_app/`**: Implementação de uma API REST completa usando Django Rest Framework.

## 📦 Tecnologias Utilizadas

- **Backend:** Django 5.x
- **API:** Django Rest Framework (DRF)
- **Banco de Dados:** SQLite (Desenvolvimento)
- **Integrações:** Firebase Admin SDK, Requests (para FakeStoreAPI)
- **Frontend:** Django Templates com CSS Customizado

## ⚙️ Como Executar

1. **Instalar Dependências:**
   ```bash
   pip install django djangorestframework firebase-admin requests Pillow
   ```

2. **Migrações:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Criar Administrador:**
   ```bash
   python manage.py createsuperuser
   ```

4. **Rodar o Servidor:**
   ```bash
   python manage.py runserver
   ```

---
*Desenvolvido como modelo de excelência em arquitetura Django.*
