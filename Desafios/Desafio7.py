n1 = float(input("Escreva a sua nota:\n"))
n2 = float(input("Escreva a sua segunda nota:\n"))
if n1 <= 10 and n2 <= 10:
    média = (n1 + n2) / 2
    print(f"Sua média é \033[4;34;40m {média}")
else:
    print("Impossivel sua nota ser maior do que 10")


