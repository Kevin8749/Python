Altura = float(input("Digite a sua altura:\n"))
Peso = float(input("Digite o seu peso:\n"))
Altura_Quadrado = Altura ** 2
Imc = Peso / Altura_Quadrado
if Imc <= 18.5:
    print("Você está abaixo do peso")
elif Imc <= 25:
    print("Peso ideal")
elif Imc <= 30:
     print("Peso Sobrepeso")
elif Imc <= 40:
    print("Obesidade")
else:
    print("Obsidade mórbida")
print(f"O IMC dessa pessoa é : {Imc:.2f}")