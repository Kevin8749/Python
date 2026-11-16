Lista_Limpa = []
Lista_Impar = []
Lista_Par = []
while True:
    Escolha = int(input("Digite um valor: "))
    Lista_Limpa.append(Escolha)
    if Escolha % 2 == 0:
        Lista_Par.append(Escolha)
    else:
        Lista_Impar.append(Escolha)
    while True:
        Escolha_Player = input("Quer continuar?[S/N] ").upper()
        if Escolha_Player == "S":
            break
        elif Escolha_Player == "N":
            break
        else:
            print("Escolha inválida")
    if Escolha_Player == "N":
        break
print(f"A lista completa é {Lista_Limpa}")
print(f"A lista de pares é {Lista_Par}")
print(f"A lista de ímpares é {Lista_Impar}")