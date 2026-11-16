num = int(input("\033[1;33;40m Escreva um número:\n"))

for i in range(1, 11):
    resultado = num * i
    print(f"O seu número {num} x {i} é igual a: {resultado}")