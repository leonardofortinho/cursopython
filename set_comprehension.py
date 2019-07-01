"""
Set Comprehension

Lista = [1, 2, 3, 4, 5]
Set = {1, 2, 3, 4, 5}
"""

# Exemplo

numeros = {num for num in range(1, 7)}

print(numeros)

# Outro exe,mplo

numeros = {x ** 2 for x in range(10)}

print(numeros)

# Desafio.: Faça uma alteração na estrutura a cima para gerar um dicionário ao invés de set.

dicionario = {x: x ** 2 for x in range(10)}

print(dicionario)

# Exemplo com String

letras = {letra for letra in 'Geek University'}

print(letras)


