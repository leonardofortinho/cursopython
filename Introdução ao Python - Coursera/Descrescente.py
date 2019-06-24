descrescente = True
anterior = int(input("Digite o primeiro numero da sequência: "))

valor = 1

while valor != 0 and descrescente:
    valor = int(input("Digite o próximo número da sequência: "))
    if valor > anterior:
        descrescente = False
    anterior = valor

if descrescente:
    print("A sequência está em ordem decrescente!")
else:
    print("A sequência não está em ordem decrescente!")
