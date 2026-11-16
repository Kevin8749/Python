from math import hypot 
oposto = int(input("\033[1;31;40m Digite o oposto:\n"))
adjacente = int(input("Digite o adjacente:\n"))

hipo = hypot(oposto,adjacente)

print(f"A hipotenusa de: {oposto} e de {adjacente} é {hipo:.2f}")