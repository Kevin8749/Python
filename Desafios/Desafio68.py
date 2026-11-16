import random
Par_Impar = 0
Vitorias = 0
while True:
    Escolha_pc = random.randint(0,100)
    print(Escolha_pc)
    Escolha_Player = input("Escolha, impar ou par: ").upper()
    Escolha_Player_num = int(input("Digite o seu número: "))
   
    Par_Impar = Escolha_Player_num + Escolha_pc
    if Escolha_Player == "PAR":
       if Par_Impar % 2 == 0:
           print("Jogador vence, mais um vitória!")
           Vitorias += 1
       else:
           print("jogador infelizmente perdeu!")
           break
    elif Escolha_Player == "IMPAR":
        if Par_Impar % 2 != 0:
            print("Jogador vence, mais um vitória!")
            Vitorias += 1
        else:
            print("jogador infelizmente perdeu!")
            break
    else:
        print(f"{Escolha_Player} não é impar ou par")
print(f"Você fez o total de {Vitorias} Vitorias")