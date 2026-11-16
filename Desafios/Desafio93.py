
nome = input("Nome do Jogador: ")
quantidade = int(input(f"Quantas partidas {nome} jogou? "))
Carreira = {"nome": nome}
Gols = []
Totais = 0
for cont in range(0,quantidade):
    gols = int(input(f"Quantos gols na partida {cont}? "))
    Totais += gols
    Gols.append(gols)
Carreira["gols"] = Gols
Carreira["total"] = Totais
print("-=" * 25)
print(Carreira)
print("-=" * 25)
for k,v in Carreira.items():
    print(f"O campo {k} tem o valor {v}")
    print("-=" * 25)
print(f"O jogador {Carreira["nome"]} jogou: {quantidade} partidas.")
for pos, v in enumerate(Carreira["gols"]):
    print(f"Na partida {pos}, fez: {v} gols")
print(f"Foi um total de {Carreira['total']} gols.")