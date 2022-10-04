"""
Zip - Unido iteráveis - não precisa importar nada para utilizar
Zip_longest - Itertools
"""

# Exemplo 1 - com zip
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']  # Monte Belo será ignorado por não ter o estado definido
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(cidades, estados)  # zip juntou as duas listas em uma unica lista
print(list(cidades_estados))
print()
# outra opçao com for
# for valor in cidades_estados:
#     print(valor)

# Exemplo 2 - com zip_longest
from itertools import zip_longest
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']  # Vai incluir e preencher com None
estados = ['SP', 'MG', 'BA']

cidades_estados = zip_longest(cidades, estados)
print(list(cidades_estados))

