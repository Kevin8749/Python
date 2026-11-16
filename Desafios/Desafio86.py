# Inicializando uma matriz 3x3 vazia com zeros
matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Preenchendo a matriz linha por linha, coluna por coluna
for linha in range(3):
    for coluna in range(3):
        valor = int(input(f"Digite um valor para a posição [{linha},{coluna}]: "))
        matriz[linha][coluna] = valor
     

# Exibindo a matriz formatada linha por linha

for linha in matriz:
    print(linha)
