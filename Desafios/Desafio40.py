Nota = float(input("Digite a sua nota de português:\n"))
Nota2 = float(input("Digite a sua nota de matemática:\n"))

média = (Nota + Nota2) / 2

if média < 5:
    print("\033[4;31;40m Reprovado! \033[m")
elif média <= 6.99:
    print("\033[4;36;40m Recuperação! \033[m")
elif média >= 7:
    print("\033[4;32;40m Aprovado! \033[m")
print("Sua média foi {}".format(média))