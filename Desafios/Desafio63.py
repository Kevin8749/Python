n = int(input("Digite algum número que mostrei a fibonnaci: \n")) 
Cont = 3
Num_Atual = 0
Proximo_Num = 1
print(f"{Num_Atual} -> {Proximo_Num} ", end="")
while Cont <= n:
    Fibonnaci = Num_Atual + Proximo_Num
    print(f"-> {Fibonnaci} ", end="")
    Num_Atual = Proximo_Num
    Proximo_Num = Fibonnaci
    # Aqui a gente guarda o próximo e atualiza os dois ao mesmo tempo
    
    Cont += 1

print("Fim")