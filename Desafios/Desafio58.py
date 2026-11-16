import random 
Tentativa = 1
Escolha_Computador = random.randint(0,10)

while True:
    Escolha = int(input("Digite o número que você acha que o computador digitou(0-10):\n"))
    if Escolha == Escolha_Computador:
        print(f"Parabéns, você conseguiu, e com: {Tentativa} tentativas")
        break
    else:
        print("Errado")
        Tentativa += 1
        if Escolha > Escolha_Computador:
            print("\033[4;32;40m Menos... Tente mais uma vez \033[m")
        elif Escolha < Escolha_Computador:
             print("\033[4;33;40m Mais... Tente mais uma vez \033[m")

