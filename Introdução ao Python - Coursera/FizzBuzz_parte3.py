numero = int(input("Digite um numero: "))

divide1 = numero % 5
divide2 = numero % 3

if divide1 == 0 and divide2 == 0: 
    print("FizzBuzz")
else:
    print(numero)
