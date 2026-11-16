from datetime import date
Maior = 0
Menor = 0
Ano = date.today().year
for Idade in range(1,8):
    print()
    Nascimento = int(input(f"Em que ano {Idade} * pessoa nasceu? "))
    if Ano - Nascimento >= 18:
        Maior += 1
    else:
         Menor += 1
print(f"O total de pessoas menores é: {Menor} \n o total de pessoas de Maiores é: {Maior}")