"""
Módulo Collections - Counter (contador)

https://docs.python.org/3.7/library/collections.html#collections.Counter

Collection -> High-performance Container Datatypes

Counter -> Recebe um interável como parãmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contendo como chave e o elemento da lista passada como parâmetro e como valor
a quantidade de ocorrências desse elemento.

# Realizando o import

from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer interável, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)

print(res)
print(type(res))
# Resultado Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 66: 3, 45: 2, 43: 1, 34: 1})
# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrencias

# Exemplo 2

print(Counter('Leonardo Luchini'))
# Resultado Counter({'L': 2, 'o': 2, 'n': 2, 'i': 2, 'e': 1, 'a': 1, 'r': 1, 'd': 1, ' ': 1, 'u': 1, 'c': 1, 'h': 1})
"""

# Realizando o import

from collections import Counter

# Exemplo 3

texto = """Sweetener é o quarto álbum de estúdio da cantora estadunidense Ariana Grande, 
lançado em 17 de agosto de 2018 através da Republic Records. As sessões de gravação e composição iniciaram em julho de 
2016, meses após o lançamento de Dangerous Woman. Grande queria experimentar novas direções musicais e, para isso, 
contou com a ajuda do compositor e produtor Pharrell Williams, com quem primeiramente desenvolveu "Sweetener", 
que definiu a musicalidade e o tema do álbum, além de servir como seu título, uma mensagem de transformar uma situação 
ruim numa melhor. As gravações foram interrompidas com o atentado ocorrido em 22 de maio de 2017 durante um show da 
Dangerous Woman Tour em Manchester; no período de pausa da turnê, a artista sofreu ataques de pânico e ansiedade, 
o que acabou inspirando uma série de novas canções, boa parte delas desenvolvidas com a equipe do produtor sueco 
Max Martin, seu parceiro Ilya e o compositor Savan Kotecha, colaboradores de longa data da cantora."""

palavras = texto.split()
# print(palavras)

res = Counter(palavras)
print(res)

# Encontrando as "5" palavras com mais ocorrências no texto.
print(res.most_common(10))
