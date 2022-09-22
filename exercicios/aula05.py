"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.
"""

def ola_mundo():
    return 'olá mundo!'


def mestre(funcao):
    return funcao()

print(ola_mundo())
print()

"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.
Faça a função1 executar duas funções wue recebam um número diferente de argumentos.
"""

def mestre(funcao, *args, **kwargs):  # *args está repassando, qualquer argumento ou **kwargs, qualquer argumento nomeado
    return funcao(*args, **kwargs)   # para a função


def fala_oi(nome):
    return f'oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando = mestre(fala_oi, 'Jessica')
executando2 = mestre(saudacao, 'Jessica', saudacao='Bom dia!')
print(executando)
print(executando2)
