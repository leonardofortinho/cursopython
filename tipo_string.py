"""
Tipo String

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre  aspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Sempre que estiver entre aspas duplas -> "uma string", "234", "a", "True", "42.3"" \
- Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''
- Estiver entre aspas duplas triplas ->

Se usar o "\n" se pula uma linha

nome = 'Hello World!'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Leonardo \nLuchini'
print(nome)
print(type(nome))

nome = 'Leonardo \" Luchini'
print(nome)
print(type(nome))

nome = 'Leonardo Luchini'
print(nome.upper()) # O "upper" deixa tudo maiusculo

nome = 'Leonardo Luchini'
print(nome.lower()) # O  "lower" deixa tudo minusculo

nome = 'Leonardo Luchini'
print(nome.split()) # O "split" separa e coloca em uma lista

# [  0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ,  7 ,  8 ,  9 , 10 , 11 , 12 , 13 , 14 , 15 ]
# [ 'L', 'e', 'o', 'n', 'a', 'r', 'd', 'o', ' ', 'L', 'u', 'c', 'h', 'i', 'n', 'i']
nome = 'Leonardo Luchini'
print(nome[0:8])  # Slice de string

print(nome[9:16])  # Slice de string

# [      0    ,     1    ]
# [ 'Leonardo', 'Luchini']
print(nome.split()[0])

print(nome.split()[1])
"""
# Estiver entre aspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

#nome = """#Leonardo pula uma linha também se fazer dessa forma.
#Luchini"""  # dessa forma também pula uma linha (coloquei sinal de "#" para comentar e não executar o programa.
#print(nome)
#print(type(nome))"""


"""
[::-1] -> Comece do primeiro elemento, vá até o último elemento e inverta
"""
nome = 'Leonardo Luchini'

print(nome[::-1])
print(type(nome))

print(nome.replace('L', 'F'))  # Substitui uma letra por outr no caso o L pelo F

texto = 'socorram me subino onibus em marrocos'  # palindromo
print(texto)

print(texto[::-1])
