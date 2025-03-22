from .models import *
from rest_framework import serializers

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class TipoPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPedido
        fields = '__all__'