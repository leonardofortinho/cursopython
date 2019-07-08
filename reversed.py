"""
Reversed

OBS.: Não confunda com a função reverse() que estudamos nas listas.

A função reverse(0 só funciona em listas. Já a função reversed() funciona em qualquer iteravel. Sua função é inverter
o iterável.

A função reversed() retorna um iterável chama List Reverse Iterator
"""

# Exeplos

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

# Podemos converter o elemento retornando para uma Lista, Tupla ou Conjunto

# Lista
lista = [1, 2, 3, 4, 5]
print(list(reversed(lista)))

# Tupla
tupla = [1, 2, 3, 4, 5]
print(tuple(reversed(tupla)))

# Conjunto. Lembrando que 'set' não define ordem dos elementos.
conjunto = [1, 2, 3, 4, 5]
print(set(reversed(conjunto)))

# Podemos iterar sobre o reversed()
for letra in reversed('Geek University'):
    print(letra, end='')

print('\n')  # Pula linha
# Podemos fazer o mesmo sem o uso do 'for'
print(''.join(list(reversed('Geek University'))))

# Já vimos como fazer isso mais fácil com slice de trings
print('Geek University'[::-1])

# Podemos também utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)

# Apesar que já vimos como fazer isso utilizando o prórpio range()
for n in range(9, -1, -1):
    print(n)
