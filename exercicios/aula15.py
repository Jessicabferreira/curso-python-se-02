"""
Geradores, Iteradores e Iteráveis em Python
"""

# Exemplo 1
lista = [1, 2, 3, 4]
iterador = iter(lista)
print(next(iterador))  # 1   next vai iterar manualmente através de todos os itens
print(next(iterador))  # 2
print(iterador.__next__())  # 3
print(iterador.__next__())  # 4
next(iterador)  # Sem mais itens para iterar, erro StopIteration ocorre
print()

# Exemplo 2 - forma mais simples de iterar usando o for
#
# for elemento in lista:
#     print(lista
#
# Exemplo 3 - função gerador
#
# def gerador():
#     for e in range(5):
#         yield e
#
# for item in gerador():
#     print(item)
#