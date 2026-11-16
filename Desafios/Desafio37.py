
Num = int(input("Escolha um número:\n"))
print("1- Conversão para binário")
print("2- Conversão para octonol")
print("3- Conversão para hexadecimal")
Num_Escolhido = int(input("\n"))
if Num_Escolhido == 1:
    print(f"Esse número em binário: {bin(Num)}")
elif Num_Escolhido == 2:
    print(f"Esse número em octonol: {oct(Num)}")
elif Num_Escolhido == 3:
    print(f"O seu número em hexadecimal é: {hex(Num)}")
else:
    print("Não existe está opção")