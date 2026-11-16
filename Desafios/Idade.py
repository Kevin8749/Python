Dinheiro = float(input("Digite o quanto você tem para gastar: "))
Precos_Produtos = [60,30,5]
Passar_Indes = 0
while True:
    Produtos = Precos_Produtos[Passar_Indes]
    Valor_int = Dinheiro // Produtos
    Valor_Sobra = Dinheiro % Produtos
    Dinheiro = Valor_Sobra
    if Dinheiro > 0 and Passar_Indes < len(Precos_Produtos):
        print(f"Você consegue comprar {Valor_int:.0f} de {Produtos} R$")
    else:
        break
    Passar_Indes += 1
print(f"Você consegue comprar {Valor_int:.0f} de {Produtos} R$")