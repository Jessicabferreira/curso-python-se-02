"""
      Exemplos simples para entender as funçoes

1 - Crie uma função que exibe uma saudação com os parâmetros saudação e nome.
"""

def saudacao(saudacao, nome):
    print(f'{saudacao} {nome}')

saudacao('Olá', 'Joãozinho')
saudacao('Olá', 'Maria')
saudacao('Olá', 'Jessica')
print()

"""
2 - Crie uma função que recebe 3 números como parâmetros e exibe a soma entre eles.
"""
def soma(n1, n2, n3):
    print(n1 + n2 + n3)

soma(2, 1, 76)
soma(15, 24, 3)
soma(27, 5, 1)
print()

"""
3 - Crie uma funçaõ que recebe 2 números. O primeiro é um valor e o segundo um percentual (ex. 10%). retorne o valor
do primeiro número somado d aumento do percentual do mesmo.
"""
def aumento_percentual(valor, percentual):
    return valor + (valor * percentual / 100)


ap = aumento_percentual(50, 10)
print(ap)
ap = aumento_percentual(100, 10)
print(ap)
ap = aumento_percentual(10, 10)
print(ap)
ap = aumento_percentual(15, 100)
print(ap)
print()

"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""
def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'fizzbuzz, {n} é divisível por 3 e 5'
    if n % 5 == 0:
        return f'buzz, {n} é divisível por 5'
    if n % 3 == 0:
        return f'fizz, {n} é divisível por 3'
    return n


from random import randint

for i in range(100):
     aleatorio = randint(0, 100)
     print(fb(aleatorio))

