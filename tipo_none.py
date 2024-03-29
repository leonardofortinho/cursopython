"""
Tipo None

O tipo de dado None em Python representa o tipo sem tipo, ou poderia ser conhecido também como tipo vazio,
porém, falar que é tipo sem tipo é mais apropriado.

Obs.: O tipo None é SEMPRE especificado com a primeira letra maiúscula.

Certo: None
Errado: none

Quando utilizamos

- Podemos utilizar quando queremos criar uma variável e inicializa-la com um tipo sem tipo, antes de recebermos um valor
final.
- O tipo None SEMPRE vai ser falso no Python
"""

numeros = None
print(numeros)
print(type(numeros))

numeros = 1.44, 1.34, 5.67

print(numeros)
print(type(numeros))