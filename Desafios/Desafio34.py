Salario_Value = float(input("Escreva o seu salário que te darei um aumento:\n"))
Salario_Aumento_Maior = Salario_Value * 0.10 + Salario_Value
Salario_Aumento_Menor = Salario_Aumento_Maior * 0.15 + Salario_Value
if Salario_Value <= 1250:
    print(f"Seu novo salário é: {Salario_Aumento_Menor}")
else:
    print(f"Seu novo salário é: {Salario_Aumento_Maior}")