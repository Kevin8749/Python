from random import randint
from time import sleep
from operator import itemgetter
maior = 0
menor = 0
segundo = 0
Escolha_1 = randint(1,6)
Escolha_2 = randint(1,6)
Escolha_3 = randint(1,6)
Escolha_4 = randint(1,6)
Jogadores = {"Jogador1": Escolha_1, "Jogador2": Escolha_2, "Jogador3": Escolha_3, "Jogador4": Escolha_4}
print("Valores sorteados")
for k,v in Jogadores.items():
    sleep(1)
    print(f"O {k} tirou {v}")
ranking = []
ranking = sorted(Jogadores.items(), key=itemgetter(1), reverse=True)
print("Ranking ficou assim:")

for pos, v in enumerate(ranking):
        sleep(1)
        print(f'O {pos + 1} º lugar: {v}')