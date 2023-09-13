hora1 = int(input("Digite o horário de entrada:"))
minuto1 = int(input("Digite os minutos de entrada:"))
hora2 = int(input("Digite o horário de permanencia:"))
minuto2 = int(input("Digite os minutos de permanencia:"))
horam = 0
if hora1 >= 12:
    hora1 = hora1 - 12
if hora2 >= 12:
    hora2 = hora2 - 12


minutot = minuto1 + minuto2
if minutot >= 60:
     minutot = minutot - 60
     horam = 1
horat = hora1 + hora2 + horam


print(f"O Horário de saída foi as {horat}:{minutot}:")
