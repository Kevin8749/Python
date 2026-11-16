

while True:
    Num = int(input("Digite um número: "))
    if Num <= 0:
        print(f"Impossivel fazer a tabuada de {Num} até 10!")
        break
    for mul in range(1,11):
        Result = Num * mul
        print(f"{Num} X {mul} é: {Result}")
        mul += 1
   
       
