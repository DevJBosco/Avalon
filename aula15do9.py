contador = 0
soma = 0
contadorp = 0
for x in range (1,11,1):
    n1 = int(input("Insira o números:"))
    if n1<0:
      contador += 1
      print(n1)
      soma = n1 + n1

contadorp= 10 -contador


print(f"Ao total foram identificados {contadorp} positivos!")
print(f"Ao total foram identificados {contador} negativos!")
print(f"A soma de numeros negativos deu {soma}")

