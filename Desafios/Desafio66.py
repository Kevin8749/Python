Soma = 0
Digitos = 0
while True:
    Num = int(input("Digite número que te mostrarei a soma deles(999 para o programa): "))
    if Num == 999:
        break
    else:
        Digitos += 1
        Soma += Num # Se o úsario digitar 3 passa o novo valor(3)
if Soma > 0:
    print(f" A soma de todos os valores  é: {Soma} \n e o tanto de digitos é: {Digitos}")