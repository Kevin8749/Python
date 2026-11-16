# Inicializando uma matriz 3x3 vazia com zeros
matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
Soma = 0
Soma_3_Coluna = 0
# Preenchendo a matriz linha por linha, coluna por coluna
for linha in range(3):
    for coluna in range(3):
        valor = int(input(f"Digite um valor para a posição [{linha},{coluna}]: "))
        matriz[linha][coluna] = valor
        if coluna == 2:
            Soma_3_Coluna += valor

# Exibindo a matriz formatada linha por linha
print("\nSua matriz ficou assim:")
for linha in matriz:
    print(linha)
    for Valor in linha:
        if Valor % 2 == 0:
            Soma += Valor
Maior_Coluna_2 = max(matriz[1])
print(f"A soma dos valores da terceira é: {Soma_3_Coluna}")
print(f"O maior número da segunda é: {Maior_Coluna_2}")
print(f"A soma dos valores pares é: {Soma}")   