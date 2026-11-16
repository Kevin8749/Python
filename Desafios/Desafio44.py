Valor = float(input("Preço das compras: R$"))
print(f"O valor do produto é {Valor}")
Preco_Normal = Valor
Preco_Vista = Valor - Valor * 0.10 
Preco_Cartão = Valor - Valor * 0.05
Preco_Parcelado = Valor + Valor * 0.20
while True:
 print("[1] à vista")
 print("[2] à cartão")
 print("[3] à 3x no cartão")
 Escolha_pagemento = int(input("Digite o jeito de pagar:\n"))
 if Escolha_pagemento == 1:
    print(f"Você pagara: {Preco_Vista}")
    break
 elif Escolha_pagemento == 2:
    print(f"Você pagara: {Preco_Cartão}")
    break
 elif Escolha_pagemento == 3:
    Parcela = int(input("Quantas parcelas? "))
    Total_Parcelado = Preco_Parcelado / Parcela
    print(f"Sua compra será parcelada em: {Parcela} e você pagara {Total_Parcelado:.2f} COM JUROS")
    break
 else:
    print("Não existe essa opção!")