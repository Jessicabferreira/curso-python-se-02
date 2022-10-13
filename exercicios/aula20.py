"""
 Groupby - Agrupando valores
"""

from itertools import groupby, tee

alunos = [
    {'nome': 'Jessica', 'nota': 'A'},
    {'nome': 'Pedro', 'nota': 'B'},
    {'nome': 'Maria', 'nota': 'A'},
    {'nome': 'Rita', 'nota': 'C'},
    {'nome': 'João', 'nota': 'D'},
    {'nome': 'Letícia', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'Joana', 'nota': 'A'},
    {'nome': 'André', 'nota': 'C'},
    {'nome': 'Rosemary', 'nota': 'A'},
    {'nome': 'Romeu', 'nota': 'A'},
    {'nome': 'Tatiane', 'nota': 'D'},
    {'nome': 'Fernanda', 'nota': 'B'},
    {'nome': 'Gabriele', 'nota': 'A'},
    {'nome': 'Eduarda', 'nota': 'C'},
]
ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)

    print(f'Agrupamento: {agrupamento}')

    for aluno in va1:
        print(f'\t{aluno}')

    quantidade = len(list(va2))
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')
    print()