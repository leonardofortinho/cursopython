"""
Mapas -> Conhecidos em Python como dicionários

Dicionários em Python são representados por chaves {}

receitas = {'jan': 100, 'fev': 250, 'mar': 400}
print(receitas)

# Interar sobre dicionários

for chave in receitas:
    print(chave)

for chave in receitas:
    print(receitas[chave])

for chave in receitas:
    print(f'Em {chave} recebi R$ {receitas[chave]}')

# Acessando as chaves
print(receitas.keys())

for chave in receitas.keys():  # Recomendado
    print(receitas[chave])

# Acessando os valores

print(receitas.values())

for valor in receitas.values():
    print(valor)

# Desempacotamento de dicionários

print(receitas.items())

for chave, valor in receitas.items():
    print(f'chave={chave} e valor={valor}')

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# * se os valores todos inteiros ou reais.

print(sum(receitas.values()))
print(max(receitas.values()))
print(min(receitas.values()))
print(len(receitas.values()))
"""
