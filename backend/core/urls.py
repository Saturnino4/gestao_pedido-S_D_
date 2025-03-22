from django.urls import path
from .views import *

urlpatterns = [
    path('pedido/', PedidoView.as_view()),
    path('pedido/registrar/', PedidoView.as_view()),
    # path('pedido/<int:id>/atualizar/', PedidoView.as_view()),
    # path('pedido/<int:id>/eliminar/', PedidoView.as_view()),
    path('pedido/<int:id>/aprovar/', ValidarPedidoViewApro.as_view()), 
    path('pedido/<int:id>/reprovar/', ValidarPedidoViewRepro.as_view()), 
]


