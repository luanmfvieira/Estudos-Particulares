from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db.models import Sum, Count, Avg
from django.db.models.functions import TruncMonth, TruncYear
from .models import Funcionario, SiteVenda, PedidoSite, FuncionarioDeletado
import json
from datetime import datetime, timedelta

def dashboard_home(request):
    """Página principal do dashboard"""
    # Estatísticas gerais
    total_funcionarios = Funcionario.objects.count()
    funcionarios_ativos = Funcionario.objects.filter(status='ativo').count()
    salario_total = Funcionario.objects.filter(status='ativo').aggregate(total=Sum('salario'))['total'] or 0
    salario_medio = Funcionario.objects.filter(status='ativo').aggregate(media=Avg('salario'))['media'] or 0
    
    context = {
        'total_funcionarios': total_funcionarios,
        'funcionarios_ativos': funcionarios_ativos,
        'salario_total': salario_total,
        'salario_medio': round(salario_medio, 2),
    }
    
    return render(request, 'dashboard/home.html', context)

def dados_grafico_vendas(request):
    """API para dados do gráfico de salários por cargo"""
    salarios_por_cargo = Funcionario.objects.filter(status='ativo').values('cargo').annotate(
        total_funcionarios=Count('id_funcionario'),
        salario_total=Sum('salario'),
        salario_medio=Avg('salario')
    ).order_by('-salario_total')
    
    labels = []
    dados_funcionarios = []
    dados_salarios = []
    
    for cargo in salarios_por_cargo:
        labels.append(cargo['cargo'])
        dados_funcionarios.append(int(cargo['total_funcionarios']))
        dados_salarios.append(float(cargo['salario_total']))
    
    return JsonResponse({
        'labels': labels,
        'funcionarios': dados_funcionarios,
        'salarios': dados_salarios
    })

def dados_grafico_produtos(request):
    """API para dados do gráfico de status dos funcionários"""
    status_funcionarios = Funcionario.objects.values('status').annotate(
        total=Count('id_funcionario')
    ).order_by('-total')
    
    labels = [s['status'].title() for s in status_funcionarios]
    dados = [int(s['total']) for s in status_funcionarios]
    
    return JsonResponse({
        'labels': labels,
        'dados': dados
    })

def gerenciar_dados(request):
    """Página para gerenciar dados (CRUD)"""
    funcionarios = Funcionario.objects.all().order_by('id_funcionario')
    
    context = {
        'funcionarios': funcionarios
    }
    
    return render(request, 'dashboard/gerenciar.html', context)

def adicionar_venda(request):
    """Adicionar novo funcionário"""
    if request.method == 'POST':
        Funcionario.objects.create(
            nome=request.POST['nome'],
            email=request.POST['email'],
            telefone=request.POST['telefone'],
            cargo=request.POST['cargo'],
            salario=float(request.POST['salario']),
            descricao=request.POST['descricao'],
            data_nascimento=request.POST['data_nascimento'],
            data_admissao=request.POST['data_admissao'],
            status=request.POST['status']
        )
        return redirect('dashboard:gerenciar_dados')
    
    return render(request, 'dashboard/adicionar_venda.html')

def editar_funcionario(request, id):
    """Editar funcionário existente"""
    funcionario = get_object_or_404(Funcionario, id_funcionario=id)
    
    if request.method == 'POST':
        funcionario.nome = request.POST['nome']
        funcionario.email = request.POST['email']
        funcionario.telefone = request.POST['telefone']
        funcionario.cargo = request.POST['cargo']
        funcionario.salario = float(request.POST['salario'])
        funcionario.descricao = request.POST['descricao']
        funcionario.data_nascimento = request.POST['data_nascimento']
        funcionario.data_admissao = request.POST['data_admissao']
        funcionario.status = request.POST['status']
        funcionario.save()
        return redirect('dashboard:gerenciar_dados')
    
    return render(request, 'dashboard/editar_funcionario.html', {'funcionario': funcionario})

def deletar_funcionario(request, id):
    """Mover funcionário para lixeira"""
    funcionario = get_object_or_404(Funcionario, id_funcionario=id)
    
    # Salvar na lixeira
    FuncionarioDeletado.objects.create(
        id_funcionario_original=funcionario.id_funcionario,
        nome=funcionario.nome,
        email=funcionario.email,
        telefone=funcionario.telefone,
        cargo=funcionario.cargo,
        salario=funcionario.salario,
        descricao=funcionario.descricao,
        data_nascimento=funcionario.data_nascimento,
        data_admissao=funcionario.data_admissao,
        status=funcionario.status
    )
    
    # Deletar da tabela principal
    funcionario.delete()
    return redirect('dashboard:gerenciar_dados')

def lixeira_funcionarios(request):
    """Página da lixeira de funcionários"""
    funcionarios_deletados = FuncionarioDeletado.objects.all().order_by('-data_exclusao')
    
    context = {
        'funcionarios_deletados': funcionarios_deletados
    }
    
    return render(request, 'dashboard/lixeira_funcionarios.html', context)

def restaurar_funcionario(request, id):
    """Restaurar funcionário da lixeira"""
    funcionario_deletado = get_object_or_404(FuncionarioDeletado, id=id)
    
    # Verificar se já existe funcionário com mesmo ID
    funcionario_existente = Funcionario.objects.filter(
        id_funcionario=funcionario_deletado.id_funcionario_original
    ).first()
    
    if funcionario_existente:
        # Sobrescrever funcionário existente
        funcionario_existente.nome = funcionario_deletado.nome
        funcionario_existente.email = funcionario_deletado.email
        funcionario_existente.telefone = funcionario_deletado.telefone
        funcionario_existente.cargo = funcionario_deletado.cargo
        funcionario_existente.salario = funcionario_deletado.salario
        funcionario_existente.descricao = funcionario_deletado.descricao
        funcionario_existente.data_nascimento = funcionario_deletado.data_nascimento
        funcionario_existente.data_admissao = funcionario_deletado.data_admissao
        funcionario_existente.status = funcionario_deletado.status
        funcionario_existente.save()
    else:
        # Criar novo funcionário
        Funcionario.objects.create(
            nome=funcionario_deletado.nome,
            email=funcionario_deletado.email,
            telefone=funcionario_deletado.telefone,
            cargo=funcionario_deletado.cargo,
            salario=funcionario_deletado.salario,
            descricao=funcionario_deletado.descricao,
            data_nascimento=funcionario_deletado.data_nascimento,
            data_admissao=funcionario_deletado.data_admissao,
            status=funcionario_deletado.status
        )
    
    # Remover da lixeira
    funcionario_deletado.delete()
    return redirect('dashboard:lixeira_funcionarios')

def excluir_permanente(request, id):
    """Excluir funcionário permanentemente da lixeira"""
    funcionario_deletado = get_object_or_404(FuncionarioDeletado, id=id)
    funcionario_deletado.delete()
    return redirect('dashboard:lixeira_funcionarios')

# Views para Vendas de Sites
def vendas_sites(request):
    """Página de vendas de sites"""
    sites = SiteVenda.objects.all().order_by('-data_criacao')
    pedidos = PedidoSite.objects.all().order_by('-data_pedido')[:10]
    
    context = {
        'sites': sites,
        'pedidos': pedidos,
        'total_sites': sites.count(),
        'sites_disponiveis': sites.filter(status='disponivel').count(),
        'valor_total': sites.aggregate(total=Sum('valor'))['total'] or 0
    }
    
    return render(request, 'dashboard/vendas_sites.html', context)

def adicionar_site(request):
    """Adicionar novo site"""
    if request.method == 'POST':
        SiteVenda.objects.create(
            nome_site=request.POST['nome_site'],
            valor=float(request.POST['valor']),
            descricao=request.POST['descricao'],
            status=request.POST['status']
        )
        return redirect('dashboard:vendas')
    
    return render(request, 'dashboard/adicionar_site.html')

def fazer_pedido(request, site_id):
    """Fazer pedido de site"""
    site = get_object_or_404(SiteVenda, id=site_id)
    
    if request.method == 'POST':
        PedidoSite.objects.create(
            site=site,
            cliente_nome=request.POST['cliente_nome'],
            cliente_email=request.POST['cliente_email'],
            cliente_telefone=request.POST['cliente_telefone'],
            mensagem=request.POST['mensagem']
        )
        return redirect('dashboard:vendas')
    
    return render(request, 'dashboard/fazer_pedido.html', {'site': site})

def gerenciar_pedidos(request):
    """Gerenciar pedidos"""
    pedidos = PedidoSite.objects.all().order_by('-data_pedido')
    return render(request, 'dashboard/gerenciar_pedidos.html', {'pedidos': pedidos})

def atualizar_pedido(request, pedido_id):
    """Atualizar status do pedido"""
    pedido = get_object_or_404(PedidoSite, id=pedido_id)
    
    if request.method == 'POST':
        pedido.status = request.POST['status']
        pedido.save()
        
        if pedido.status == 'aprovado':
            pedido.site.status = 'vendido'
            pedido.site.save()
    
    return redirect('dashboard:gerenciar_pedidos')