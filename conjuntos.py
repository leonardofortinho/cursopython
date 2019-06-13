"""
Conjuntos

- Conjunto em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos da matemática.

- No Python, os conjuntos são chamados de Sets.

Da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via indice, ou seja, conjuntos não são indexados.

Conjuntos são bons para se utilizar quando precisamo armazenar elementos, mas não importamos com a ordenação deles.
Quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referênciados em Python com chaves {}

Diferença entre Conjuntos (Set) e mapas (Dicionários = dict) em python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;

# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # Repare que temos valores repetidos

print(s)
print(type(s))

# Obs.; Ao criar um conjunto, caso seja adicionado já existente, o mesmo será ignorado sem gerar error e não fará parte
# do conjuntos.

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

# Importante lembrar que, além de não termos valores duplicados, não temos ordem

# Listas aceitam valores duplicados, então temos 10 elementos
lista = [99, 2, 34, 23, 2, 12, 34, 1, 44, 5]
print(f'Lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = (99, 2, 34, 23, 2, 12, 34, 1, 44, 5)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionários não aceitam chaves duplicadas, então temos 8 elementos
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 34, 1, 44, 5], 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados, então temos 8 elementos
s = {99, 2, 34, 23, 2, 12, 34, 1, 44, 5}
print(f'Conjunto: {s} com {len(s)} elementos')

# Assim como todo outro conjunto Python podemos colocar todos os tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)

# Usos interessantes com sets

# Imagine que fizemos um formulário de cadastro de visitantes em um feira ou museu, e os visitantes informam manualmente
# a cidade de onde vieram.

# Nós adicionamos em uma lista python já que em uma lista podemos adicionar novos elementos e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas temos.
# O que você faria? Faria um loop na lista?

# Podemos utilizar o set para isso:

print(len(set(cidades)))

# Adicionando elementos em um conjunto
s = {1, 2, 3}
print(s)

s.add(4)
s.add(4)  # Duplicidade não gera erro, simplesmente é ignorado e não é adicionado.
print(s)

# Remover elementos em conjuntos
s = {1, 2, 3}
print(s)

# Forma 1
s.remove(3)  # Não é indice! Informamos o valor a ser removido.
print(s)

# Obs.: Caso o valor não seja encontrado, será gerado erro KeyError. Nenhum valor é retornado.

# Forma 2

s.discard(2)
print(s)

# Obs.: Se o valor não for encontrado, nennhum erro é gerado.

# Copiando um conjunto para outro

s = {1, 2, 3}
print(s)

# Forma 1 - Deep Copy

novo = s.copy()
print(novo)

novo.add(4)
print(novo)
print(s)

# Forma 2 - Shallow Copy

novo = s
novo.add(4)

print(novo)
print(s)

# Podemos remover todos os itens de um conjunto

s = {1, 2, 3}
print(s)

s.clear()
print(s)

# Métodos Matemáticos de Conjuntos

# Imagine que temos 2 conjuntos: um contendo estudantes do curso Python e um contendo estudantes do curso Java.

estudantes_python = {'Marco', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam python também estudam Java.

# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando union (Recomendado)

unicos1 = estudantes_python.union(estudantes_java)
# Resultado: {'Fernando', 'Patricia', 'Gustavo', 'Julia', 'Pedro', 'Guilherme', 'Ellen', 'Ana', 'Marco'}
print(unicos1)

# Forma 2 - Utilizando o caractere pip |

unicos2 = estudantes_python | estudantes_java
# Resultado: {'Ellen', 'Julia', 'Guilherme', 'Ana', 'Gustavo', 'Pedro', 'Patricia', 'Fernando', 'Marco'}
print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Utilizando intersection

ambos1 = estudantes_python.intersection(estudantes_java)
# Resultado {'Julia', 'Patricia'}
print(ambos1)

# Forma 2 - Utilizando o &

ambos2 = estudantes_python & estudantes_java
# Resultado {'Julia', 'Patricia'}
print(ambos2)

# Gerar um conjunto de estudantes que não estão no outro curso

so_python = estudantes_python.difference(estudantes_java)
# Resultado {'Guilherme', 'Ellen', 'Marco', 'Pedro'}
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
# Resultado {'Gustavo', 'Fernando', 'Ana'}
print(so_java)

# Soma*, Valor máximo*, Valor mínimo*, Tamanho
# * se todos os valores forem inteiros ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
"""

