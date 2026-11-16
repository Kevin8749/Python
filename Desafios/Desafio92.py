from datetime import date
nome = input("Nome: ").capitalize()
ano_nascimento = int(input("Ano de nascimento: "))
Carteira = int(input("Carteira de Trabalho (0 não tem): "))
if Carteira != 0:
    Ano_contratacao = int(input("Ano de contratação: "))
    Salario = float(input("Salário: R$ "))
    # Pegar a idade
    Idade = date.today().year - ano_nascimento
    aposentadoria = Idade + 35
    Cadastro = {"nome": nome, 
            "idade": Idade, 
            "ctps": Carteira, 
            "contratação": Ano_contratacao,
            "Aposentodaria": aposentadoria
            }
    print("-=" * 30)
    for cadastro in Cadastro.items():
        print(cadastro)
    for key,value in Cadastro.items():
        print(f"{key} tem o valor {value}")