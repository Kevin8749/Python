Pessoas_18 = 0
Homens = 0
Mulheres_Menores_20 = 0
while True:
    Sexo = input("Digite o seu sexo(M/F): ").upper()
    
    if Sexo == "M" or Sexo == "F":
        Idade = int(input("Digite a sua idade: "))
        while True:
            Resposta = input("Deseja continuar?[S/N]: ").strip().upper()
            if Resposta == "S" or Resposta == "N":
                  break
            else:
                  print("Dado inválido")
        if Idade >= 18:
              Pessoas_18 += 1
        if Sexo == "M":
                Homens += 1
        if Sexo == "F" and Idade < 20:
                Mulheres_Menores_20 += 1
        if Resposta == "N" or Resposta == "NÃO":
                break
        else:
             print("Dado inválido")
    else:
        print("Dado inválido")
        
print(f"O total de pessoas com 18 anos ou mais são {Pessoas_18} e o total de homens é: {Homens} e total de mulheres menores de 20 é: {Mulheres_Menores_20}")
    
    