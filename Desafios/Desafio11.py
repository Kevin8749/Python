Base = float(input("\033[10;31;40m Escreva a base da sua parede:\n"))
Altura = float(input("Escreva a largura da sua parede:\n"))
Area = Base * Altura
tinta_por_litro = 2
total = int(Area / tinta_por_litro)
print("Você gastara: {:.2f} balde de tinta".format(total))