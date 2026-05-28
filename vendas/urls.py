from django.urls import path
from . import views

urlpatterns = [
    path('comprar/<int:produto_id>/', views.realizar_compra, name='realizar_compra'),
]
