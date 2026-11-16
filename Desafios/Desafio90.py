Escolha_Nome = str(input("nome: ")).capitalize()
Escolha_Média = float(input(f"média de {Escolha_Nome}: "))
Aluno = {"Nome": Escolha_Nome, "Média": Escolha_Média}
Cor_Red = "\033[1;31;40m"
Cor_Green = "\033[1;32;40m"
print(f"Nome é igual a: {Aluno['Nome']}")
print(f"Média é igual a: {Aluno['Média']}")
if Aluno["Média"] >= 7:
    print(f"{Cor_Green} Situação é igual a: APROVADO\033[m!")
else:
    print(f"{Cor_Red} Situação é igual a: REPROVADO\033[m!")