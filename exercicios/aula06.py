"""
Expressões lambda (funções anônimas) em Python
"""
# Exemplo 1
preco = 1000

def calcular_imposto(preco):
    return preco * 0.3          # return dá como resposta tal informação

print(calcular_imposto(preco))
print()


# Exemplo 2  -  Não é preciso criar uma função para poder aplicar
calcular_imposto2 = lambda x: x * 0.3  # recebe informaçaõ x e te da como resposta x * 0.3

print(calcular_imposto2(preco))     # é parecido com codigo a acima más com menos linhas
