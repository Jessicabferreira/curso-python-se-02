"""
 Funções (def) em python - Parte 3)

*args, são argumentos
**kwargs, são argumentos com palavras chaves
"""

# Exemplo 1
def func(*args):    # args, empacotameneto e desempacotamento
    print(args)

lista = [1,2,3,4,5]
n1, n2, *n = lista    # n1 e n2 está desempacotando apartir do *n está empacotando
print(n1, n2, n)
print()

# Exemplo 2
def func(*args):
    print(args)

lista = [1,2,3,4,5]
print(*lista, sep='-')
print()

# Exemplo 3
def func(*args):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))

func(1,2,3,4,5)
print()

# Exemplo 4
def func(*args):
    print(args)

lista = [1,2,3,4,5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2)  # as duas listas vão ser mescladas dentro do args sem separação
print()

# Exemplo 5
def func(*args, **kwargs):
    print(args)
    print(kwargs['nome'], kwargs['sobrenome'])  # argumentos com palavras chaves

lista = [1,2,3,4,5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Jessica', sobrenome='Ferreira')  # argumentos nomeados que são estão dentro do kwargs
