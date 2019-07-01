"""
Utilizando Lambdas

Conhecidas por Expressões Lambdas, ou simplesmente, Lambdas, são funções sem nome, ou seja funções anônimas.

# Exemplo de Função em Python

def função(x):
    return 3 * x + 1


print(função(4))

# Expressão Lambda

lambda x: 3 * x + 1

# E como utilizar a expressão lambda?

calc = lambda x: 3 * x + 1  # Não é a forma ideal (PEP 8)

print(calc(4))

# Podemos ter expressões lambdas com mútiplas entradas

# Strip tira espaço da variável. Mas não tira o espaço entre uma variável e outra.
# Title vai colocar letra maiúscula na primeira letra da variável.
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' angelina', 'JOLIE'))
print(nome_completo(' FELICITY        ', ' jones '))

# Em funções Python podemos ter nenhuma ou várias entradas. Em lambda também:

amar = lambda: 'Como não amar python? '

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 /x + 1 / y + 1 / z)

# n = lambda x1, x1, ..., xn: <expressão>

print(amar())
print(uma(6))
print(duas(5, 7))
print((tres(3, 6, 9)))

# OBS.: Se passarmos mais argumentos que parâmetros esperados, teremos TypeError.

# Outro Exemplo

autores = ['Issac Asimov', 'Ray Brandbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)
"""

# Função Quadrática
# f(x) = a * x ** + b * x + c

# Definindo a função


def gerador_funcao_quadrtica(a, b, c):
    """Retorna a função f(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c


teste = gerador_funcao_quadrtica(2, 3, -5)
print(teste(0))
print(teste(1))
print(teste(2))

print(gerador_funcao_quadrtica(3, 0, 1)(2))




