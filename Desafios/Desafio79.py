Lista = []
while True:
    Escolha_Num = int(input("Digite um número: "))
  
    if Escolha_Num in Lista:
        print("Este número já está na lista!")
    else:
        Lista.append(Escolha_Num)
        print("Valor adicionado com sucesso")
    Escolha = input("Deseja continuar[S/N]? ").upper()
    if Escolha == "S":
        print()
    elif Escolha == "N":
        print("Finalizando")
        break
Lista.sort()
print(f"Seus valores em ordem crescente ficou: {Lista}")