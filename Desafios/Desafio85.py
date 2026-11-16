temp = [[], []] # temp[0] vai ser o impares e o temp[1] vai ser os pares😎

for i in range(1,8):
    Escolha = int(input(f"Digite o {i} º valor: "))
    if Escolha % 2 == 0:
        temp[1].append(Escolha)
    else:
        temp[0].append(Escolha)
temp[1].sort()
temp[0].sort()
print(f"Os valores pares digitados foram: {temp[1]} 😎")
print(f"Os valores ímpares digitados foram: {temp[0]} 😎")