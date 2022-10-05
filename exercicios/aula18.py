"""
Count - Itertools
vai retornar um iterador
"""
# Exemplo 1
from itertools import count

contador = count(start=5, step=2)  # start de onde quero iniciar / step pular de 2 em 2

for valor in contador:
    print(valor)

    if valor >= 30:
        break  # quebra do laço
print()

# Exemplo 2
from itertools import count

contador = count()                                     # a cada elemento adicionado sem precisar mexer no contador
lista = ['Luiz', 'João', 'Maria', 'José', 'Eduardo']   # eu ja vou ter um novo indice para o novo elemento.
lista = zip(contador, lista)  # Indexar a lista
print(list(lista))
