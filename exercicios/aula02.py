"""
  Funções - def em python - return - (Parte 2)
"""

# Exemplo 1
def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2

divide = divisao(8,4)

if divide:
    print(divide)
else:
    print('Conta inválida.')
print()

# Exemplo 2
def dumb():
    return 1.1

var = dumb()
print(var, type(var))
print()

# Exemplo 3
def dumb():
    return ('Luiz', 'Otávio')

var = dumb()

print(var, type(var))
