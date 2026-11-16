Escolha = input("Digite a expressão: ")
Escolha = Escolha.replace(" ", "")
ùltimo_Indece = len(Escolha)
if  "(" in Escolha[0] and ")" in Escolha[:]:
     print("Expressão válida!")

else:
     print("Expressão inválida")
    