Record = 0
Num_Menor = 0
media = 0
Total_Valores = 0
Num_Antigo = True
while True:
    Escolha_Num = int(input("Digite um número: "))
    Escolha_Player = input("Deseja continuar? (S/N): ").upper()

    media += 1
    Total_Valores += Escolha_Num
    if Num_Antigo:
        Record = Escolha_Num
        Num_Menor = Escolha_Num
        Num_Antigo = False
    else:
        if Escolha_Num > Record:
            Record = Escolha_Num
        if Escolha_Num < Num_Menor:
            Num_Menor = Escolha_Num
    if Escolha_Player == "N" or Escolha_Player == "NÃO":
        break
print(f"O maior número é: {Record} e o menor é: {Num_Menor} \n e a média de números é: {Total_Valores / media:.0f}")