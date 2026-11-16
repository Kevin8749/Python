Pessoas = []
Pessoa = {}
Mulheres = []
Total = 0
Idade_Total = 0
while True:
    Total += 1
    nome = input("Nome: ")
    sexo = input("Sexo: ").upper()
    idade = int(input("Idade: "))
    resposta = input("Deseja continuar[S/N]? ").upper()
    Pessoa["nome"] = nome
    Pessoa["sexo"] = sexo
    Pessoa["idade"] = idade
    Idade_Total += Pessoa["idade"]
    Pessoas.append(Pessoa.copy())
    if Pessoa["sexo"] == "F":
        Mulheres.append(Pessoa["nome"])
    if resposta == "N":
        break
media = Idade_Total / Total
print(f"- O grupo tem {Total} pessoas.")
print(f"- A média de idade é de {media} anos.")
print(f"- As mulheres cadastradas foram: {Mulheres}")
print(f"- Lista das pessoas que estão acima da média:")
for v in Pessoas:
    if v["idade"] > media:
        print(f"nome = {v["nome"]}; sexo = {v["sexo"]}; idadade = {v["idade"]} ")
print("<< ENCERRADO >>")