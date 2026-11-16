import random 
n1 = str(input("\033[0;33;40m Primeiro aluno:\n"))
n2 = str(input("Segundo aluno:\n"))
n3 = str(input("Terceiro aluno:\n"))
n4 = str(input("Quarto aluno:\n"))
lista = [n1,n2,n3,n4]
Escolhido = random.choice(lista)

print(f"O aluno escolhido para apagar o quadro foi o aluno: {Escolhido}")
