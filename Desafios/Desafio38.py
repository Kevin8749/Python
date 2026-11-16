
Num1 = int(input("Digite um número: "))
Num2 = int(input("Digite um outro número: "))

#print(max(Num1, Num2)

if Num1 > Num2:
    print(f"\033[4;32;40m O  Primeiro número é maior do que o segundo número \033[m")
elif Num2 > Num1:
     print(f"\033[4;32;40m O Segundo número  é maior do que o Primeiro número\033[m")
else:
      print(f"\033[1;35;40m O dois valores são iguais \033[m")
