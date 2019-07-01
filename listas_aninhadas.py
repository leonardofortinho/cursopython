"""
Listas Aninhadas (Nested List)

- Algumas linguagens de programação(C/Java) possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays/Veteros);
    - Multidimensionais (Matrizes);

Em Python nós temos as Listas

numeros = [1, 'b', 3.234, True, 5]

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3

print(listas)
print(type(listas))

# Como fazemos para acessar os dados?

print(listas[0][1])  # Acesso a primeira linha a coluna 2
print(listas[2][1])  # Acesso a terceira linha a coluna 8
print('')

# Iterando com loops em uma lista aninhada
for lista in listas:
    for num in lista:
        print(num)

# Lista Comprehension
print('')
[[print(valor) for valor in lista] for lista in listas]
"""

# Outros Exemplos

# Gerando um tabuleiro/matriz 3x3
# O primeiro cria as linhas [] e o segundo as colunas []
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais

print([['*' for i in range(1, 4)] for j in range(1, 4)])


