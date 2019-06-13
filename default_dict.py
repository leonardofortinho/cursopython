""""
Módulo Collections - Default Dict

https://docs.python.org/3.7/library/collections.html#collections.defaultdict

Recapitulando dicionário

dicionario = {'curso': 'Programação em Python: Essencial'}

print(dicionario)
print(dicionario['curso'])
print(dicionario['outro'])  # KeyError, porque não existe a chave.

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default, podendo utilizar
um lambda para isso. Este valor será utilizado sempre que um valor definido. Caso tentarmos acessar
uma chave que não existe, essa chave será criada e o valor default será atribuído.

Obs.: Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada e retornar valores.
"""

# Fazendo import do Default Dict

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

print(dicionario)

dicionario['curso'] = 'Programação em Python: Essencial'

print(dicionario)

print(dicionario['outro'])  # Não acontece o KeyError, por causa da função lambda

print(dicionario)

