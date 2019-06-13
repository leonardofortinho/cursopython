"""
Recebendo dados do usuário

input() => Todo o dado recebido via input é do tipo String

Em python, string é tudo que estiver entre:
- Aspas simples; Ex: 'Leonardo'
- Aspas duplas; Ex: "Leonardo"
- Aspas simples triplas; Ex: '''Leonardo'''
"""
#- Aspas duplas triplas; Ex: """Leonardo"""
"""
"""
# Entrada de dados
# print("Qual seu nome? ")
# nome = input()  # Input -> entrada de dados

nome = input("Qual seu nome? ")

# print("Qual sua idade: ")
# idade = input()

idade = int(input("Qual sua idade? "))

# Processamento

# Saída de dados

# Exemplo de print antigo, versão python 2.x

# print("Seja bem-vindo(a) %s" % nome)
# print("O %s tem %s ano" % (nome, idade))

# Exemplo moderno, da nova versão 3.x

# print("Seja bem-vindo(a) {0}".format(nome))
# print("O {0} tem {1} anos".format(nome, idade))

# Exemplo de print "mais atual" 3.7

print(f"Seja bem-vindo(a) {nome}")

print(f"A {nome} tem {idade} anos")

"""
# int(idade) => cast

Cast é a "conversão" de um tipo de dado para outro.
"""

print(f"A {nome} nasceu em {2018 - idade}")


