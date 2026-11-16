Nums = []
Numeros_Digitado = 0
while True:
    Num_Escolhido = int(input("Digite um valor: "))
    if not Nums:
        Nums.append(Num_Escolhido)
        Numeros_Digitado += 1
    else:
        Inserido = 0
        for pos,v in enumerate(Nums):
            if Num_Escolhido > v:
                Nums.insert(pos,Num_Escolhido)
                Inserido += 1
                Numeros_Digitado += 1
                break
        if Inserido == 0:
            Nums.append(Num_Escolhido)
            Numeros_Digitado += 1
    while True:
        Escolha_Player = input("Quer continuar[S/N]? ").upper()
        if Escolha_Player == "S":
            break
        elif Escolha_Player == "N":
            break
        else:
            print("Opção inválida")
    if Escolha_Player == "N":
        break
print(f"VocÊ digitou: {Numeros_Digitado} elementos")
print(Nums)
if 5 in Nums:
    print("O valor 5 faz parte da lista")
else:
    print("O valor 5 não faz parte da lista")
