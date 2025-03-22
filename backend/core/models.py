from django.db import models

# Create your models here.
class Pedido(models.Model):
    empresa_nome = models.CharField(max_length=100)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    tipo_pedido_id = models.ForeignKey('TipoPedido', on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='pendente')
    class Meta:
        db_table = 'pedido'
    def __str__(self):
        return self.empresa_nome
    
class TipoPedido(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    class Meta:
        db_table = 'tipo_pedido'
    def __str__(self):
        return self.nome
    
class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    class Meta:
        db_table = 'empresa'
    def __str__(self):
        return self.nome
    
    
    

