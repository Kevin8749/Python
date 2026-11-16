import random
# Escolher entre 4 alunos para aprensentar o trabalho, o primeiro(ex): maria, Segunado: jorge, Terceiro: mario, 4: lola
n1 = str(input("\033[1;34;40m Primeiro aluno:\n"))
n2 = str(input("Segundo aluno:\n"))
n3 = str(input("Terceiro aluno:\n"))
n4 = str(input("Quarto aluno:\n"))
Ordem = [n1,n2,n3,n4] # {}

random.shuffle(Ordem)
print(f"A ordem escolhida foi:\n {Ordem}")