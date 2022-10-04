"""
Zip - Unindo iteráveis - não precisa importar nada para utilizar
Zip_longest - Itertools - precisa ser importado
"""

# Exemplo 1 - com zip
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']  # Monte Belo será ignorado por não ter estado definido
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(cidades, estados)  # zip uniu as duas listas em uma unica lista
print(list(cidades_estados))
print()
# outra opçao com for
# for valor in cidades_estados:
#     print(valor)

# Exemplo 2 - com zip_longest
from itertools import zip_longest
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip_longest(cidades, estados)  # inclui o Monte Belo e preenche com None por não ter estado definido
print(list(cidades_estados))

