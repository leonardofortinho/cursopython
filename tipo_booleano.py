"""
Tipo Booleano

Algebra Booleana, criada por Geroge Boole

2 constantes, Verdadeiro ou Falso

No Python:
True: Verdadeiro
False: Falso

Obs.: Sempre a inicial maiuscula

Errado: true, false

Certo:

True, False
"""

ativo = False

print(ativo)

"""
Operação Básicas
"""

# Negação (not):
"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso, se for falso o resultado será verdadeiro,
ou seja, sempre o contrário.
"""
print(not ativo)

logado = False

# Ou (or):
"""
É uma operação vinária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro.

print(True or True) -> True
print(True or False) -> True
print(False or True) -> True
print(False or False) -> False
"""
print(ativo or logado)

# E (and):
"""
Também é uma operação binária, ou seja, depende de dois valores. Ambos os valores devem ser verdadeiros.

True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""