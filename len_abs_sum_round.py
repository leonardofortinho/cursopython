"""
Len, Abs, Sum e Round

# Len
len() -> Retorna o tamanho (ou seja) o número de itens de um iterável.

# Só pra revisar:
# String
print(len('Geek University'))
# List
print(len([1, 2, 3, 4, 5]))
# Tuple
print(len((1, 2, 3, 4, 5)))
# Set
print(len({1, 2, 3, 4, 5}))
# Dict
print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))
# Range
print(len(range(0, 10)))

# Por debaixo dos panos quando utilizamos a função len(), o Python faz o seguinte:

# Dunder len
print('Geeek University'.__len__())

# Abs
abs() - > Retorna o valor absoluto de um número interio ou real. De forma básica, seria o seu valor real sem o sinal.

# Exemplos Abs

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

# abs() não funciona para uma string.

# Sum
sum() -> Recebe como parâmetro um interável, podendo receber um valor inicial, e retorna a soma total de elementos,
incluindo o valor inicial

OBS.: O valor inicial default = 0

# Exemplos de Sum

# Lista
print(sum([1, 2, 3, 4, 5]))
# Com valor inicial '5'
print(sum([1, 2, 3, 4, 5], 5))
# Com valor inicial '-5'
print(sum([1, 2, 3, 4, 5], -5))
# Float
print(sum([3.145, 5.678]))
# Tuple
print(sum((1, 2, 3, 4, 5)))
# Set
print(sum({1, 2, 3, 4, 5}))
# Dict
print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))

# sum() não pode somar strings

# Round
round() -> Retorna um número arredondado para n digito de precisão após a casa decimal. Se a precisão não for informada
retorna o interio mais próximo da entrada.

# Exemplos Round

print(round(10.2))  # Inteiro
print(round(10.5))  # Inteiro
print(round(10.6))  # Inteiro
print(round(1.21212121, 2))  # Real
print(round(1.219999999, 2))  # Real
"""






