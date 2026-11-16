Maior_Peso = []
for Peso in range(1,5+1):
    Pessoa_Peso = float(input(f"Peso da {Peso} º pessoa:\n"))
    Maior_Peso.append(Pessoa_Peso)
print(f"O maior peso é: {max(Maior_Peso)}")
print(f"O menor peso é: {min(Maior_Peso)}")