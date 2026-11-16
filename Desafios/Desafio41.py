from datetime import date
Ano_Atual = date.today().year
Ano_Atleta = int(input("Digite quando vocÊ nasceu:\n"))
Idade_Atleta = Ano_Atual - Ano_Atleta

if Ano_Atleta > Ano_Atual:
    print("Está viajando no futuro??")
else:
   if Idade_Atleta <= 9:
    print("\033[4;32;40m Classificação: Mirim \033[m")
   elif Idade_Atleta <= 14:
    print("\033[4;33;40m  Classificação: Infantil \033[m")
   elif Idade_Atleta <= 19:
    print("\033[4;34;40m  Classificação: Junior \033[m")
   elif Idade_Atleta <= 25:
    print("\033[4;35;40m  Classificação: Sênior \033[m")
   else:
    print("\033[1;36;40m  Classificação: MASTER!     \033[m")
print(f"Sua idade é: {Idade_Atleta} anos.")