Pessoal = []
Dados = []
Maior = 0
Menor = 0
while True:
    Dados.append(str(input("Nome: ")))
    Dados.append(float(input("Peso: ")))
    if len(Pessoal) == 0:
        Maior = Dados[1]
        Menor = Dados[1]
    else:
        if Dados[1] > Maior:
            Maior = Dados[1]
        if Dados[1] < Menor:
            Menor = Dados[1]
    Pessoal.append(Dados[:])
    Dados.clear()
    resp = input("Deseja continuar? [S/N] ").upper()
    if resp in "N":
      break
print(f"O maior pesso foi: {Maior} KG da pessoas: ", end="")
for p in Pessoal:
    if p[1] == Maior:
        print(f"{p[0]}")
print()
print(f"O menor pesso foi: {Menor} KG da pessoas: ", end="")
for pe in Pessoal:
    if pe[1] == Menor:
        print(f"{p[0]}")
print()
print(f"Ao todo, voce cadastrou {len(Pessoal)} pessoas")

