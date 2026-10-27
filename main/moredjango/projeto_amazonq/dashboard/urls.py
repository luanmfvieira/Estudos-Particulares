from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_home, name='home'),
    path('api/vendas/', views.dados_grafico_vendas, name='api_vendas'),
    path('api/produtos/', views.dados_grafico_produtos, name='api_produtos'),
    path('gerenciar/', views.gerenciar_dados, name='gerenciar_dados'),
    path('adicionar/', views.adicionar_venda, name='adicionar_venda'),
    path('funcionario/editar/<int:id>/', views.editar_funcionario, name='editar_funcionario'),
    path('funcionario/deletar/<int:id>/', views.deletar_funcionario, name='deletar_funcionario'),
    
    # URLs para vendas de sites
    path('vendas/', views.vendas_sites, name='vendas'),
    path('sites/adicionar/', views.adicionar_site, name='adicionar_site'),
    path('sites/pedido/<int:site_id>/', views.fazer_pedido, name='fazer_pedido'),
    path('pedidos/', views.gerenciar_pedidos, name='gerenciar_pedidos'),
    path('pedidos/atualizar/<int:pedido_id>/', views.atualizar_pedido, name='atualizar_pedido'),
    
    # URLs para lixeira
    path('lixeira/', views.lixeira_funcionarios, name='lixeira_funcionarios'),
    path('restaurar/<int:id>/', views.restaurar_funcionario, name='restaurar_funcionario'),
    path('excluir-permanente/<int:id>/', views.excluir_permanente, name='excluir_permanente'),
]