from math import ceil as Aument
total_De_Pessoas = 0
Total_Mulheres = 0
Média = 4
Idade_total = -1
Nome = ""
for Pessoas in range(1,2 + 1):
    print(f"===== {Pessoas} º =====")
    nome = str(input("Digite o seu nome: "))
    Idade = int(input("Digite a sua idade: "))
    Sexo = str(input("Sexo [M/F]: ")).upper()
    total_De_Pessoas += Idade
    if Sexo == "F" and Idade >= 20:
        Total_Mulheres += 1
    if Sexo == "M":
       if Idade > Idade_total:
           Idade_total = Idade
           Nome = nome
print(f"No grupo há: {Total_Mulheres} de mulheres acima ou igual de 20 anos")
print(f"A média de idade do grupo é de: {Aument(total_De_Pessoas / Pessoas)}")
if Idade != -1:
    print(f"O homem mais velho do grupo é {Nome} e ele tem: {Idade_total}")
else:
    print("Nenhum homem pode ter menos de 0 anios")