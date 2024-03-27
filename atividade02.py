  cont = 0    
notas = 10
soma = 0

while cont < notas:
    nota = float(input(f" Informe a nota {cont}: "))
    soma = soma + nota
    cont = cont + 1

media = soma/notas
print(f"a média é {media:.2f}")

if media >=7:
    print("aprovado")
elif media >=4 and media < 7:
    print("Exame final")
else:
    print("Reprovado")
