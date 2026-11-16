

def Move():
    print("Andando para frente")

def Ré():
    print("Dando ré")

def Esquerda():
    print("Esquerda")

def Direita():
    print("Direita")

while True:
 Acao = str(input("Digite a sua ação:\n"))
 if Acao == "Frente":
    Move()
    break
 elif Acao == "Ré":
    Ré()
    break
 elif Acao == "Esquerda":
    Esquerda()
    break
 elif Acao == "Direita":
     Direita()
     break
 else:
    print("Não existe essa ação")
    
    