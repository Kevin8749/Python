Numeros = []
for i in range(5):
    Escolha = int(input("Digite um valor: "))
    if not Numeros:
        Numeros.append(Escolha)
    else:
        Inserido = False
        for pos,num in enumerate(Numeros):  
            if Escolha < num:
                Numeros.insert(pos, Escolha)
                print(f"Adicionada na pocisão {pos} da lista...")
                Inserido = True
                break
        if not Inserido:
            Numeros.append(Escolha)
            print("Adicionado no final da lista...")
print(Numeros)
        