from datetime import date
Idade = int(input("Digite o ano de nascimento:\n"))
Ano_Atual = date.today().year
Maior_Idade = Ano_Atual - Idade
print(Maior_Idade)
if Maior_Idade == 18:
    print("Você já pode se alistar")
elif Maior_Idade < 18:
    Anos_Faltam = 18 - Maior_Idade
    Ano_Alistamento = Ano_Atual + Anos_Faltam
    print(f"Quem nasceu em: {Idade} tem: {Maior_Idade} em 2026")
    print(f"Falatam: {Anos_Faltam} para seu alistamento")
    print(f'Seu alistamento será em {Ano_Alistamento}')
else:
    Anos_Passaram = Maior_Idade - 18
    Anos_Alistamento = Ano_Atual -  Anos_Passaram
    print(f"Quem nasceu em: {Idade} tem: {Maior_Idade}")
    print(f"Você deveria ter se alistado há: {Anos_Passaram} anos")
    print(f"Seu alistemento foi em: {Anos_Alistamento}")
