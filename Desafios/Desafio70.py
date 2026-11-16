Nome_barato = "Vazio kk"
Primeiro_Digito = True
Produto_Mais_Barato = 0
Quantidade_1k = 0
Total_De_Gasto = 0
while True:
    Name = input("Digite o nome do seu produto: ")
    Preco = float(input("Digite o preço do seu produto: "))
    Resposta = input("Deseja continuar?[S/N]: ").strip().upper()
    Total_De_Gasto += Preco
    if Primeiro_Digito:
        Nome_barato = Name
        Produto_Mais_Barato = Preco
        Primeiro_Digito = False
        if Preco >= 1000:
            Quantidade_1k += 1
        if Resposta == "N":
            break
        
    else:
        if Preco < Produto_Mais_Barato: # Verificação de produto
            Produto_Mais_Barato = Preco
            Nome_barato = Name
        if Preco >= 1000:
            Quantidade_1k += 1
        if Resposta == "N":
            break
print(f"O total da comprar foi de R${Total_De_Gasto} \n Temos {Quantidade_1k} produtos custando mais de 1000 R$ \n O produto mais barato foi {Nome_barato} que custa: {Produto_Mais_Barato:.2f}")