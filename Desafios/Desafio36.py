Valor_da_casa = float(input("Qual o valor da casa que o senhor deseja pegar um empréstimo?\n"))
Salario_Comprador = float(input("Qual o seu salário?:\n"))
Ano = int(input("Em quantos anos você vai pagar:\n"))

MesesTotais = Ano * 12
Prestacao = Valor_da_casa / MesesTotais
Porcentagem_Salario = Salario_Comprador * 0.30

if Prestacao <= Porcentagem_Salario:
    print("Empréstimo aprovado")
else:
    print("Empréstimo negado")
    print(f"Para você pagar essa casa de {Valor_da_casa} em {Ano} ano você tem que ter: {Prestacao:.2f}")