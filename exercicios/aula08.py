"""
Dicionários em python
Estrutura de dados que suporta um par de chaves e valor
"""

dados_cliente = {
    'Nome': 'Jessica',
    'Endereco': 'Rua Cruzeiro do Norte',
    'Telefone': '977245978',
    'Email': '*****@gmail.com'
}

print(dados_cliente['Nome'])
print(dados_cliente)

dados_cliente['Idade'] = 55  # adicionar elementos, fazer uma nova chave
print(dados_cliente)
