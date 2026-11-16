while True:
    Sexo = str(input("Digite o seu sexo(M/F): \n")).upper()
    if Sexo == "M" or Sexo == "F":
        print(f"O seu sexo é {Sexo}")
        break
    else:
        print(f"O seu sexo {Sexo} é inválido")