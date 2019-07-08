"""
Sorted

OBS.: Não confunda, apesar do nome, com a função sort() que já estudamos em listas. O sort() só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável:

Como o próprio nome diz, sorted() serve para ordenar elementos.

OBS.: O sroted() SEMPRE retorna uma lista com os elementos do iterável ordenados

# Exemplo

numeros = [6, 1, 8, 2]
print(numeros)
print(sorted(numeros))  # Ordenar do menor para o maior.
print(numeros)
print()
numeros = (6, 1, 8, 2)
print(numeros)
print(sorted(numeros))  # Ordenar do menor para o maior.
print(numeros)
print()
numeros = {6, 1, 8, 2}
print(numeros)
print(sorted(numeros))  # Ordenar do menor para o maior.
print(numeros)

# Adicionando parãmetros ao sorted()

numeros = [6, 1, 8, 2]
print(numeros)
print(sorted(numeros))
print(sorted(numeros, reverse=True))  # Nesse caso ele ordena do maior para o menor.

print(tuple(sorted(numeros)))
print(sorted(numeros, reverse=True))  # Nesse caso ele ordena do maior para o menor.

print(set(sorted(numeros)))
print(sorted(numeros, reverse=True))  # Nesse caso ele ordena do maior para o menor.

# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "amarelo"},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [], "cor": "preto", "musica": "rock"},
]

print(usuarios)

# Ordenando por username
print(sorted(usuarios, key=lambda usuario: usuario["username"]))  # Tem que informar a chave (key) do dicionário
                                                                  # para ele ordenar.

# Ordenando por tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["username"])))


print(sorted(usuarios, key=lambda usuario: usuario["username"], reverse=True))
print(sorted(usuarios, key=lambda usuario: usuario["username"], reverse=False))
"""

# Último exemplo

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock in roll, too young to die", "tocou": 32}
]

# Ordenar da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica ['tocou']))

# Ordenar da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica ['tocou'], reverse=True))



