"""
Funções com Parâmetro Padrão (Default Parameters)

- Funções onde a passagem de parametro seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional

print('Leonardo Luchini')
print()

# Exemplo de função onde a passagem de função é obirgatório

def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado()) # vai dar typeerror

def exponecial(numero=4, potencia=2):
    return numero ** potencia


# Colocando o "=2" ele torna o item valor padrão, caso não seja informado, sera elevado ao numero informado. Isso pode
# ser feito no "numero" colocando o "=4", deixando também com o valor padrão.

print(exponecial(2, 3))  # 2 * 2 * 2 = 6
print(exponecial(3, 2))  # 3 * 3 = 9

print(exponecial(3))  # Por padrão eleve ao quadrado
print(exponecial(3, 5))  # Eleva à potência informada pelo usuário

# OBS.: Se o usuário passara somente 1 parâmetro, este será atríbuido ao parâmetro numero, e será calculado
# o quadrado desdete número;
# Se o usuário passar 2 argumentos, o primeiro será atribuido ao parâmetro número e o segundo ao parâmetro potência.
# Então será calculada está potência.

# OBS.: Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração.

# ERRO!
#def teste(num=2, potencia):
#    return num ** potencia


# CORRETO!
def teste(potencia, num=2):
    return num ** potencia


print(teste(6))

def soma(num1=0, num2=0):
    return num1 + num2


print(soma(4, 3))
print(soma(4))
print(soma())

def mostra_informacao(nome='Leonardo', instrutor=False):
    if nome == 'Leonardo' and instrutor:
        return 'Bem Vindo instrutor Leonardo'
    elif nome == 'Leonardo':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Geek'))
print(mostra_informacao(nome='José'))

# Por quê utilizar parâmetros com valor default?

- Nos permite ser mais flexíveis nas funções;
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de código;

# Quais tipos de dados podemos utilizar como valores default para parâmetros?

- Qualquer tipo de dado:
    - Números, strings, floats, booleanos, listas, tuplas, dicionários, funções etc;

# Exemplos


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))


# Escopo - Evitar problemas e confusões...

# Variáveis globais

instrutor = 'Leonardo'  # Variável global

def diz_oi():
    instrutor = 'Python'
    return f'Oi {instrutor}'


print(diz_oi())

# OBS.: Se tivermos uma variável local com o mesmo nome de uma variável global, a local, terá a preferência.

# Variáveis locais

def diz_oi():
    prof = 'Leonardo'  # Variável local
    return f'Olá {prof}'


print(diz_oi())

print(prof)  # NameError

# ATENAÇÃO com variáveis globais (se puder evitar, evite!)

total = 0

def incrementa():
    total = total + 1
    return total


print(incrementa())  # UnboundLocalError (A vairável local está sendo utilizada para processamento
                     # sem ter sido inicializada

Vairaveis Globais

# ATENAÇÃO com variáveis globais (se puder evitar, evite!)

total = 0

def incrementa():
    global total  # Avisando que queremos utilizar a variável global
    total = total + 1
    return total


print(incrementa())
print(incrementa())
print(incrementa())

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável

def fora():
    contador = 0

    def dentro():
        nonlocal contador  # O nonlocal usa a variável do "fora", não global, mas não é local da função dentro
        contador = contador + 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())
"""

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável

def fora():
    contador = 0

    def dentro():
        nonlocal contador  # O nonlocal usa a variável do "fora", não global, mas não é local da função dentro
        contador = contador + 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())




