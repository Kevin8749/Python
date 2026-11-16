import random 
from time import sleep
print("Digite pedra, papel ou tesoura")
lista = ["tesoura", "pedra", "papel"]
Escolha_Pc = random.choice(lista)

Escolha_Player = str(input()).strip().lower()

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")

if Escolha_Player == "tesoura" and Escolha_Pc == "papel":
    print(f"Parabéns, você ganhou!")
elif Escolha_Player == "pedra" and Escolha_Pc == "tesoura":
    print("Parabéns, você ganhou")
elif Escolha_Player == "papel" and Escolha_Pc == "pedra":
    print("Parabéns, você ganhou")
elif Escolha_Player == Escolha_Pc:
    print(f"Empate")
else:
    print(f"Você perdeu")
print(f"O computador jogou {Escolha_Pc}")
print(f"Jogador jogou {Escolha_Player}")