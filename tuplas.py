"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem básicamente duas diferenças básicas:

- As tuplas são representadas por parênteses ()
- As tuplas são imutáveis: isso significa que ao se criar uma tupla ela não muda. Toda operação em um tupla gera
uma nova tupla.

# CUIDADO 1: as tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(type(tupla1))
print(tupla1)

tupla2 = 1, 2, 3, 4, 5, 6
print(type(tupla2))
print(tupla2)

# CUIDADO 2: tuplas com 1 elemento

tupla3 = (4)  # Isso não é uma tupla!
print(type(tupla3))
print(tupla3)


tupla4 = (4,)  # Isso é uma tupla!
print(type(tupla4))
print(tupla4)

tupla5 = 4,  #
print(type(tupla5))
print(tupla5)

# Conclusão: Podemos concluir que tuplas são definidas pela vírgula (,) e não pelo uso do parênteses

(4) -> Não é tupla
(4,) -> É tupla
4, -> É tupla

# Podemos gerar uma tupla dinamicamente com range(inicio:fim:passo)
tupla = tuple(range(11))
print(type(tupla))
print(tupla)

# Desempacotamento de tupla

tupla = ('Leonardo Luchini', 'Filipe Luchini')

irmao1, irmao2 = tupla

print(irmao1)
print(irmao2)

# Obs.: Gera erro (VelueError) se colocarmos um número diferente de elementos para desempacotar.

# Métodos para: adição e remoção de elementos nas tuplas, não existem, dado o fato das tuplas serem imutáveis.

# Soma*, Valor Máximo*, Valor Mínimo*, e Tamanho
# * Se os valores forem interiros ou reais

tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)  # Tuplas são imutaveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)

tupla1 = tupla1 + tupla2  # Tuplas são imutaveis, mas podemos sobrescrever seus valores.
print(tupla1)

# Verificar se determindao elemento está contido na tupla

tupla = (1, 2, 3)
print(3 in tupla)

# Iterando sobre um tupla

tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('c'))

nome = tuple('Leonardo Luchini')
print(nome)
print(nome.count('o'))

# Dicas na utilização de tuplas

# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro'
, 'Dezembro')

# O acesso a elementos de um tupla também é semelhante a de uma lista

print(meses[5])

# Iterar com while
i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificamos em qual indice um elemento está na tupla

print(meses.index('Junho'))

# Obs.: Caso o elemento não existe vai ser gerado um erro.

# Verificamos em qual indice um elemento está na tupla

print(meses.index('Junho'))

# Obs.: Caso o elemento não existe vai ser gerado um erro.

# Slicing
# tupla[inicio:fim:passo]

print(meses[5:9])

# Por quê utilizar tuplas?

# - Tuplas são mais rápidas do que listas
# - Tuplas deixam seu código mais seguro*. (* isso porque trabalhar com elementos imutáveis traz segurança para o código

# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla  # Na tupla não temos o Shallow Copy (listas)

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra

print(nova)
print(tupla)
"""