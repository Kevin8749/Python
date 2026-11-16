from random import randint
from time import sleep
numeros = []
def sortear():
    print("Sorteando 5 valores da lista: ", end=" ")
    for valor in range(5):
        Num = randint(0,20)
        numeros.append(Num)
        print(f"{Num}",end = " ",flush=True)
        sleep(0.40)
    print("PRONTO!")
def Soma(lst):
    soma = 0
    for valor in lst:
        if valor % 2 == 0:
            soma += valor
    print(f"Somando os valores pares de {lst}, temos {soma}")
print(numeros)
sortear()
Soma(numeros)

