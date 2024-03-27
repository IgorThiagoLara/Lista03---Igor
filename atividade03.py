#Exercício 3
pares = 0
impares = 0
somaPares = 0
somaImpares = 0

while pares < 5 and somaImpares <= 30:
    numero = int(input("Digite um número inteiro: "))

    if numero < 0:
        print("Esse número não é positivo, tente novamente")
        continue

    if numero % 2 == 0:
        print(f"o número {numero} é par")
        pares = pares + 1
        somaPares = somaPares + numero

    else:
        print(f"O número {numero} é ímpar")
        impares = impares + 1
        somaImpares = somaImpares + numero
    
print(f"O número total de pares digitados foi: {pares}")
print(f"O número total de ímpares digitados foi: {impares}")
print(F"A soma dos números pares é: {somaPares}")
print(f"A soma entre os números pares e ímpares é: {somaImpares}")
