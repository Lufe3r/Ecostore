from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_produtos, name='lista_produtos'),
    path('<int:pk>/', views.detalhe_produto, name='detalhe_produto'),
]
