from random import sample as Sorteio
from time import sleep

Sorteios = []

print("-=" * 15)
print("     JOGO DA MEGA SENA!       ")
print("-=" * 15)

Escolha_Player = int(input("Quantas rodadas você quer sortear? "))

if Escolha_Player <= 10:
    print(f"   SORTEADO {Escolha_Player} JOGOS")
    for c in range(1, Escolha_Player + 1):
        print("-=" * 15)
        
        Mega = Sorteio(range(1, 61), 6)
        Mega.sort()
        # Transformando a lista em texto sem colchetes para exibir
        sleep(1)
        print(f"Jogo {c}: {Mega}")
else:
    print(f"O número: {Escolha_Player} são muitos sorteios!")

print("-=" * 15)
print("Boa sorte!")