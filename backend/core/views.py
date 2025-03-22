from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Pedido
from .serializers import PedidoSerializer
from django.shortcuts import get_object_or_404

def responseData(data=None, status=200, message=None):
    response = {
        'status': status,
        'message': message,
        'data': data
    }
    return Response(response, status=status) #, json_dumps_params={'ident': 4})

def queryPedido(id):
    try:
        return get_object_or_404(Pedido, id=id)
    except Exception as e:
        return None
# Create your views here.


class PedidoView(APIView):
    def get(self, request):
        try:
            pedidos = Pedido.objects.all()
            serializer = PedidoSerializer(pedidos, many=True)
            return responseData(data=serializer.data, message='Lista de pedidos')
        except Exception as e:
            return responseData(status=400, message=str(e))
        
    def post(self, request, id=None):

        if 'validade' in request.path and id is not None:
            return self.validate(request, id)

        try:
            pedido = request.data
            if 'valor' in pedido and pedido['valor'] > 1000:
                pedido['status'] = 'pendente'
            else:
                pedido['status'] = 'aprovado'
            # Create an article from the above data
            serializer = PedidoSerializer(data=pedido)
            if serializer.is_valid(raise_exception=True):
                pedido_saved = serializer.save()
            return responseData(data=PedidoSerializer(pedido_saved).data, message='Pedido criado com sucesso')
        except Exception as e:
            return responseData(status=400, message=str(e))

    # def validate(self, request, id):
    #     try:
    #         pedido = queryPedido(id)
    #         if pedido is None:
    #             return responseData(status=404, message='Pedido não encontrado')

    #         if pedido.valor > 1000:
    #             pedido.status = 'aprovado'
    #         else:
    #             pedido.status = 'reprovado'
    #         pedido.save()
    #         return responseData(data=PedidoSerializer(pedido).data, message='Pedido validado com sucesso')
    #     except Exception as e:
    #         return responseData(status=400, message=str(e))    

    def put(self, request, id):
        try:
            saved_pedido = get_object_or_404(Pedido.objects.all(), id=id)
            data = request.data
            serializer = PedidoSerializer(instance=saved_pedido, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                pedido_saved = serializer.save()
            return responseData(data=PedidoSerializer(pedido_saved).data, message='Pedido atualizado com sucesso')
        except Exception as e:
            return responseData(status=400, message=str(e))
        
    def delete(self, request, id):
        try:
            pedido = get_object_or_404(Pedido.objects.all(), id=id)
            pedido.delete()
            return responseData(message='Pedido excluído com sucesso')
        except Exception as e:
            return responseData(status=400, message=str(e))

class ValidarPedidoViewApro(APIView):

    def post(self, request, id):
        pedido = get_object_or_404(Pedido, id=id)

        pedido.status = 'aprovado'  # Pode ser alterado para um status que indique revisão manual
        
        pedido.save()
        return responseData(data=PedidoSerializer(pedido).data, message='Pedido Aorovado com sucesso')

class ValidarPedidoViewRepro(APIView):

    def post(self, request, id):
        pedido = get_object_or_404(Pedido, id=id)

        pedido.status = 'reprovado'  # Pode ser alterado para um status que indique revisão manual
        
        pedido.save()
        return responseData(data=PedidoSerializer(pedido).data, message='Pedido Reprovado com sucesso')