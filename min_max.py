"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos.

# Exemplos max()

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))

tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla))

conjunto = {1, 8, 4, 99, 34, 129}  # Set
print(max(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario))  # Se colocar só o dicionário, ele só vai dizer qual é a maior chave, que no caso é o 'f'

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario.values()))

print(max(3, 34))

# Faça um programa que receba dois valores do usuário e mostre o maior.
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(max(val1, val2))

print(max(4, 67, 54))
print(max('a', 'ab', 'abc'))
print(max('a', 'b', 'c', 'd', 'g'))
print(max(3.145, 5.789))
print(max('Geek University'))  # Ele vai pegar o 'y' porque está mais para o final do alfabeto.


min() -> Retorna o menor valor de dois ou mais elementos.

# Exemplos min()

lista = [1, 8, 4, 99, 34, 129]
print(min(lista))

tupla = (1, 8, 4, 99, 34, 129)
print(min(tupla))

conjunto = {1, 8, 4, 99, 34, 129}  # Set
print(min(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario))  # Se colocar só o dicionário, ele só vai dizer qual é a menor chave, que no caso é o 'a'

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario.values()))

print(min(3, 34))

# Faça um programa que receba dois valores do usuário e mostre o menor.
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(min(val1, val2))

print(min(4, 67, 54))
print(min('a', 'ab', 'abc'))
print(min('a', 'b', 'c', 'd', 'g'))
print(min(3.145, 5.789))
print(min('Geek University'))  # Ele vai pegar o ' ' (espaço), por ser o menor da string.

# Outros Exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

# Ele segue a linha de ordem alfabética
print(max(nomes))
print(min(nomes))

# Neste exemplo ele conta o número de tamanho do nome.
print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))
"""

# Exemplos mais complexos

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock in roll, too young to die", "tocou": 32}
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# DESAFIO! Imprima somente o título da música mais e menos tocada

print(max(musicas, key=lambda titulo: titulo['tocou'])['titulo'])
print(min(musicas, key=lambda titulo: titulo['tocou'])['titulo'])

# DESAFIO! Como encontrar a música mais tocada e a menos tocada sem usar max, min ou lambda

max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])

min = 999999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])



