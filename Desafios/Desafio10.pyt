Saldo = float(input("\033[1;32;40m Digite o seu saldo:\n"))
Dolar = 5.03
result = int(Saldo / Dolar)
if Saldo >= Dolar:
    print("Você pode comprar: {:.2f} Dolares".format(result))
else:
    print("Você não pode comprar")
