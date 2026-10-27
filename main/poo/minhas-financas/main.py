from utilitarios import (
    cadastrar_categoria,
    cadastrar_transacao,
    saldo_total,
)

# categorias
categoria_receitas = cadastrar_categoria('Receitas')
categoria_contas = cadastrar_categoria('Contas')
categoria_lazer = cadastrar_categoria('Lazer')
categoria_viagens = cadastrar_categoria('Viagens')

# transacoes
cadastrar_transacao(
    descricao='Salario',
    valor=1500.0,
    categoria=categoria_receitas
)

cadastrar_transacao(
    descricao='processo',
    valor=500.0,
    categoria=categoria_receitas
)


cadastrar_transacao(
    descricao='ifood/roupas',
    valor=-400,
    categoria=categoria_lazer
)

cadastrar_transacao(
    descricao='Conta de Luz',
    valor=-220,
    categoria=categoria_contas
)

cadastrar_transacao(
    descricao='Conta de internet',
    valor=-160,
    categoria=categoria_contas
)

cadastrar_transacao(
    descricao='Faculdade',
    valor=-109,
    categoria=categoria_contas
)

cadastrar_transacao(
    descricao='Netflix+Spotify',
    valor=-50,
    categoria=categoria_contas
)

cadastrar_transacao(
    descricao='Academia',
    valor=-155,
    categoria=categoria_contas
)


cadastrar_transacao(
    descricao='Academia',
    valor=-350,
    categoria=categoria_contas
)

cadastrar_transacao(
    descricao='Disney',
    valor=0,
    categoria=categoria_viagens
)

total = saldo_total()

print('Saldo total:', total)


