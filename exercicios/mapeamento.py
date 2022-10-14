"""
Map, Filter e Reduce
"""

from dados import produtos, pessoas, lista
from functools import reduce

# Exemplo 1 - com Map
def aumento_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p


novos_produtos = map(aumento_preco, produtos)

for produto in novos_produtos:
    print(produto)
print()

nomes = map(lambda p: p['nome'], pessoas)  # Dessa forma com lambda da para pegar só os nomes ou idade

for pessoa in nomes:
    print(pessoa)
print()


# Exemplo 2 - com Filter
def filtra(pessoa):
    if pessoa['idade'] < 18:
        return True


nova_lista = filter(filtra, pessoas)  # filtrou as pessoas menores de idade

for produto in nova_lista:
    print(produto)
print()


# Exemplo 3 - com Reduce
soma_lista = reduce(lambda ac, i: i + ac, lista, 0)   # acumulando os valores dentro do ac = acumulador
print(soma_lista)