print("Analisando o Triângulo: ")

import turtle

caneta = turtle.Turtle()


r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

# Testando a condição de existência
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("Isso é um triângulo")
else:
    print("Isso não é um triângulo")