from time import sleep
def Contador(inicio,fim,passo):
    if inicio > fim and passo > 0:
        passo = -passo  
    for cont in range(inicio,fim,passo):
        print(f"\033[1;32;40m{cont}\033[m", end=" ", flush=True) 
        sleep(0.25)
    print("\033[4;32;40m Fim!\033[m")
print("Contagem de 1 até 10 de 1 em 1")
Contador(1,10,1)
print("Contagem de 10 até 0 de 2 em 2")
Contador(10,-1,-2)

print("Agora é sua vez de personalizar a contagem!")
inicio = int(input("Início: "))
Fim = int(input("Fim: "))
Passos = int(input("Passo: "))
if Passos  == 0:
    Passos = 1
    print(f"Contagem de {inicio} até {Fim} de {Passos} em {Passos}")
    Contador(inicio,Fim,Passos)
else:
    print(f"Contagem de {inicio} até {Fim} de {Passos} em {Passos}")
    Contador(inicio,Fim,Passos)