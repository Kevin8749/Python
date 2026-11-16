Num1 = int(input("Digite o primeiro número:\n"))
Num2 = int(input("Digite o segundo número:\n"))
print("Escolha uma das opções abaixo:\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa")
while True:
    Escolha = int(input("Digite sua escolha: "))
    if Escolha == 1:
         result = Num1 + Num2
         print(f"A soma dos dois valor é: {result}")
    elif Escolha == 2:
        result = Num1 * Num2
        print(f"A multiplicação dos dois valores é: {result}")
    elif Escolha == 3:
        result = max(Num1,Num2)
        print(f"O maior número dentre ele é: {result}")
    elif Escolha == 4:
        Novo_Valor = int(input("Digite o primeiro valor: "))
        Novo_Valor2 = int(input("Digite o segundo valor: "))
        Num1 = Novo_Valor
        Num2 = Novo_Valor2
    elif Escolha == 5:
        print("Saindo")
        break
    else:
         print("Essa opção não existe")   
    print("Escolha uma das opções abaixo:\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa")
    print(f"O seu resultado é: {result}") 