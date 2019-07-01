"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.

# Biblioteca para trabalhar com dados estasticos
import statistics

# Dados coletados de algun sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dadso utilizando a função mean(). O mean() é função de média.
media = statistics.mean(dados)
print(f'Media: {media}')

# OBS.: Assim como a função map() a filter() recebe dois parâmetros, sendo um função e um iterável.

res = filter(lambda valor: valor > media, dados)
print(type(res))
print(list(res))

# OBS.: Assim como na função map(), após serem utilizados os dados de filter() eles são excluídos da memória.
print(f'Novamente: {list(res)}')  # Exemplo de como a função está limpa da memória.


# Forma 1 - Usando None

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)

res = filter(None, paises)

print(list(res))

# Forma 2 - Usando lambda

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

res = filter(lambda pais: len(pais) > 0, paises)

print(list(res))

# Forma 3 - Usando lambda 2

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

res = filter(lambda pais: pais != '', paises)

print(list(res))

# A diferença entre map() e filter() é:
# map() -> Recebe dois parâmetros, uma função e um interável e retorna um objeto mapeando a função para cada
# elemento do iterável
# filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um ojeto filtrado apenas os elementos de
# acordo com a função.

# Exemplo mais complexo

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu garo"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []},
]

print(usuarios)

# Filtrar os usuários que estão inativos no Twitter

# Forma 1
# inativos = list(filter(lambda usario: len(usario['tweets']) == 0, usuarios))

# Forma 2
inativos = list(filter(lambda usario: not usario['tweets'], usuarios))

print(inativos)
"""

# Como combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é: + nome, desde de que cada nome tenha menos 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)

