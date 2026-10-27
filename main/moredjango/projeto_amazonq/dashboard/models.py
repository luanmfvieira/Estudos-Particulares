from django.db import models

class Funcionario(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    telefone = models.CharField(max_length=30)
    cargo = models.CharField(max_length=50)
    salario = models.FloatField()
    descricao = models.TextField()
    data_nascimento = models.DateField()
    data_admissao = models.DateField()
    status = models.CharField(max_length=20, default='ativo')
    
    class Meta:
        db_table = 'funcionarios'
        managed = False
    
    def __str__(self):
        return self.nome

class SiteVenda(models.Model):
    nome_site = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('disponivel', 'Disponível'),
        ('vendido', 'Vendido'),
        ('desenvolvimento', 'Em Desenvolvimento')
    ], default='disponivel')
    
    class Meta:
        db_table = 'sites_venda'
    
    def __str__(self):
        return self.nome_site

class PedidoSite(models.Model):
    site = models.ForeignKey(SiteVenda, on_delete=models.CASCADE)
    cliente_nome = models.CharField(max_length=100)
    cliente_email = models.EmailField()
    cliente_telefone = models.CharField(max_length=20)
    mensagem = models.TextField(blank=True)
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('rejeitado', 'Rejeitado'),
        ('concluido', 'Concluído')
    ], default='pendente')
    
    class Meta:
        db_table = 'pedidos_sites'
    
    def __str__(self):
        return f'{self.cliente_nome} - {self.site.nome_site}'

class FuncionarioDeletado(models.Model):
    id_funcionario_original = models.IntegerField()
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    telefone = models.CharField(max_length=30)
    cargo = models.CharField(max_length=50)
    salario = models.FloatField()
    descricao = models.TextField()
    data_nascimento = models.DateField()
    data_admissao = models.DateField()
    status = models.CharField(max_length=20)
    data_exclusao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'funcionarios_deletados'
    
    def __str__(self):
        return f'{self.nome} (Deletado)'