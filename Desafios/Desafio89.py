Alunos = []
Dados = []
while True:
    Nome = input("Digite o nome do aluno: ").capitalize()
    Nota1 = float(input("Digite a primeira nota: "))
    Nota2 = float(input("Digite a segunda nota: "))
    Escolha = input("Deseja continuar? ").upper()
    Dados.append(Nome)
    Dados.append(Nota1)
    Dados.append(Nota2)
    Média = (Dados[1] + Dados[2]) / 2
    Dados.append(Média)
    Alunos.append(Dados[0:])
    Dados.clear()
    if Escolha == "N":
        break
for valor, pe in enumerate(Alunos):
    
    print("No.     Nome      Média")
    print(f"{valor}    {pe[0]}         {pe[3]:.1f}")

while True:
    escolha_player = int(input("Qual aluno você quer mostrar? [999 para o programa]: "))
    
    if escolha_player == 999:
        print("Finalizando o programa...")
        break
    
    # Verificamos se o índice digitado existe na lista de alunos
    if 0 <= escolha_player < len(Alunos):
        aluno_selecionado = Alunos[escolha_player]
        print(f"Notas de {aluno_selecionado[0]} são: {aluno_selecionado[1]} e {aluno_selecionado[2]}")
    else:
        print("Erro: Este número de aluno não existe. Tente novamente.")