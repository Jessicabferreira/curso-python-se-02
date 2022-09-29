"""
List Comprehension
"""

# Exemplo normal
lista_precos = [500, 1500, 2000, 100, 25]

nova_lista_precos = []
for preco in lista_precos:
    nova_lista_precos.append(preco * 2)  # append adicionar valor
print(nova_lista_precos)
print()

# Exemplo com list comprehension
nova_lista_precos2 = [preco * 2 for preco in lista_precos]  # Codigo com ordem diferente, realiza a operação em uma linha
print(nova_lista_precos2)
