Primerio = int(input("Digite o primeiro valor: "))
Segundo = int(input("Digite o segundo valor: "))
Terceiro = int(input("Digite o terceiro valor: "))
Quarto = int(input("Digite o quarto valor: "))


Todos_Valores = (Primerio,Segundo,Terceiro,Quarto)
print(f"Apareceu o 9: {Todos_Valores.count(9)} vezes")
if 3 in Todos_Valores:
    print(f"O numero 3 está na pocisão: {Todos_Valores.index(3) + 1}")
else:
    print("O numero 3 não existe")
for n in Todos_Valores:
    if n % 2 == 0:
        print(f"{n}", end=" ")
