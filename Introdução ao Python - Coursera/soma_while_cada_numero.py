numero = int(input("Digite uma sequência de números: "))

soma = 0
while numero > 0:
    x = numero % 10
    numero = numero // 10
    soma = soma + x
print(soma)