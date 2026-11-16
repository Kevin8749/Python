Num = int(input("Digite um número: "))
Valor_Incial = Num

for num in range(Num - 1, 0, -1):
    print(num)
    Resul = Num
    Resul *= num
    Num = Resul
    num -= 1
    print(Resul)
print(f"O fatorial do número é: {Valor_Incial} é {Resul}")