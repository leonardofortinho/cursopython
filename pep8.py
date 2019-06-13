"""
PEP 8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python

Zen of Python

import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica.

[1] - Utilize Camel Case para nomes de classes;

Ex:

class Calculadora:
    pass


class CalculadoraCientifica:
    pass

[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis;

Ex:

def soma():
    pass

def soma_dois:
    pass

numero = 4

numero_impar = 5

[3] - Utilize quadro espaços para identação! (NÃO use tab)

Ex:

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco

- Separar funções e definições de classes com duas linhas em brancos.
- Métodos dentro de uma classe devem ser separados com uma úica linha em branco.

[5] - Imports

- Imports devem ser sempre em linhas separadas.

Ex:

#Importa Errado

import sys, os

#Import Correto

import sys
import os

# Não há problemas em utilizar:

from types import StringType, ListType

#Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e
antes de constantes ou variáveis globais.

[6] - Espaços em expressões e instruções;

# Não Façam:

funcao ( algo[ 1 ], { outro: 2 } )

#Faça:

funcao(algo[1], {outro})

#Não faça:

algo (1)

#Faça:

algo(1)

#Não faça:

dict ['chave'] = list_[indice]

#Faça:

dict['chave] = lista[indice]

#Não faça:

x              = 1
y              = 3
variavel_longa = 5

#Faça:

x = 1
y = 3
variavel_long = 5

[7] - Termine sempre um instrução com uma nova linha (em branco);
"""
import this