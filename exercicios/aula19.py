"""
Combinations, Permutatios e Product - Itertools
"""

# Exemplo 1
from itertools import combinations, permutations, product

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

for grupo in combinations(pessoas, 2):  # Combinação - Ordem não importa
    print(grupo)
print()

# Exemplo 2

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

for grupo in permutations(pessoas, 2):  # Permutação - Ordem importa
    print(grupo)
print()

# Exemplo 3

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

for grupo in product(pessoas, repeat=2):  # Ordem importa e repete valores únicos
    print(grupo)
print()
