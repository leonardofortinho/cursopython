"""
Generator Expression
Em aulas anteriores nós estudamos:
- List Comprehension;
- Dictionary Comprehension;
- Set Comprehension;

Não vimos:

- Tuple Comprehension...porque elas se chamam Generators

nomes = ['Carlos, 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes])

# Poderiamos ter feito utilizando Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))

# Lista Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

# Qual é a utilidade de getsizeof()? -> Returna a quantidade de bytes em mamória do elementos passado como parâmetro.
from sys import getsizeof

# MOstra quantos bytes a string 'Geek' está ocupando em meória. Quanto maior a string, mais espaço ocupa.
print(getsizeof('Geek'))

print(getsizeof('University'))

print(getsizeof(9))

print(getsizeof(91))

print(getsizeof(92345668823))

print(getsizeof(True))

from sys import getsizeof

# Gerando uma lista de número s com list comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de número s com set comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de número s com dictionary comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator Expression
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'Lista Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dicitionary Comprehension: {dict_comp} bytes')
print(f'Generator Expression: {gen} bytes')
"""

# Eu posso iterar no generator Expression? Sim!

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)