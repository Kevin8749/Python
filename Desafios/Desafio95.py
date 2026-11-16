Jogadores = []
while True:
    Total = 0
    Gols = []
    Carreria = {}
    nome = input("Nome do jogador: ")
    Partidas = int(input(f"Quantas partida {nome} jogou? "))
    Carreria["nome"] = nome
    for cont in range(0,Partidas):
        gols = int(input(f"Quantos gols na partida {cont}? "))
        Gols.append(gols)
        Total += gols
    Carreria["total"] = Total
    Carreria["Gols"] = list(Gols)
    Jogadores.append(Carreria.copy())
    print(Jogadores)
    resp = input("Quer continuar? [S/N] ").capitalize()
    if resp == "N":
        break
print(len(Jogadores))
for pos, jogador in enumerate(Jogadores):
    print(f"{'cod':<6} {'Jogador':<15} {'Gols':<6} {'total':<6}")
    print(f"{pos:<6} {jogador["nome"]:<15} {str(jogador["Gols"]):<6} {jogador["total"]:<6}")
while True:
    Jogador_Escolhido = int(input("Escolha um jogador pelo cod dele(999 para o programa): "))
    if Jogador_Escolhido < len(Jogadores):
        print(f" -- LEVANTAMENTO DO JOGADOR {Jogadores[Jogador_Escolhido]["nome"]}: ")
        for partida,gol in enumerate(Jogadores[Jogador_Escolhido]["Gols"]):
            print(f"No jogo {partida + 1} ele fez {gol} gols")
    elif Jogador_Escolhido == 999:
        print("Finalizando")
        break
    else:
        print("Cod inválido")
    