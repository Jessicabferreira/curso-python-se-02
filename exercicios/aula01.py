"""
 Funções - def em python (Parte 1)

função são criadas para não repetir código
pode executar quantas linhas de codigos quiser dentro da função estando dentro da hierarquia
normalmente na função não é usado o PRINT e sim o RETURN aqui é um exemplo simples antes de começar a usar o RETURN
"""

# Exemplo 1
def funcao():
    print('Olá mundo!')

funcao()
funcao()
funcao()
funcao()
print()

# Exemplo 2
def funcao(msg):  # recebe parametro
    print(msg)

funcao('Eu posso escrever o que eu quiser aqui.')
print()

# Exemplo 3
def saudacao(msg, nome):   # modifiquei o nome da funçao com refactor
    print(msg, nome)

saudacao('Olá', 'Jessica')
saudacao('Oi', 'Pedro')
saudacao('Hello', 'Maria')
saudacao('Olá', 'João')
print()

# Exemplo 4
def saudacao(msg= 'Olá', nome='usuário'):  # valores padraõ para poder utilizar funçao sem usar nenhum parametro
    print(msg, nome)

saudacao()   # função sem parametro vai ser preenchida pela função padrão
saudacao('Oi', 'Jessica')  # valores são enviados na ordem a não ser que tenha valores padrão
saudacao('Hello', 'Pedro')
saudacao('Olá', 'João')
print()

# Exemplo 5
def saudacao(msg= 'Olá', nome='usuário'):
    print(msg, nome)

saudacao(nome='Zezinho', msg='Hi')  # inverter valores nomeados
saudacao('Oi', 'Jessica')
saudacao('Hello', 'Pedro')
saudacao('Olá', 'João')
