"""
Map

Com map, fazemos mapeamento de valores para função.

import math


def area(r):
    #Calcula a área de um círculo com raio 'r'.
    return math.pi * (r ** 2)  # o uso do math.pi, pi é uma constante da biblioteca math.


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 14]

# Forma 1 - Comum
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

# Forma 2 - Usando o Map. (Map é uma função que rece dois parâmetros: o primeiro a função, o segundo um iterável.)

areas = map(area, raios)  # Map vai pegar cada elemento do rarios e jogar na area(r) da função.

print(areas)  # <map object at 0x00000193EB9A64A8>
print(type(areas))
print(list(areas))

# Forma 3 - Map com Lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS.: Após utilizar a função map(), depois da primeira utilização do resultado, ele zera.

# Para fixar - Map

# Temos dados iteráveis:

# Dados: a1, a2, ..., an

# Temos uma função:

# Funçã: f(x)

# Utilizamos a função map(f, dados) onde map irá 'mapear' cada elementos dos dados e aplicar a função.

# O Map Object: f(a1), f(a2), f(...), f(an).
"""

# Mais exemplo

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova Yorl', 28),
           ('Londres', 22)]

print(cidades)

# Fazer um calculo para Fahrenheit
# f = 9/5 * c + 32

# Lambda

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_para_f, cidades)))

