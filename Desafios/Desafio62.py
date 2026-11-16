print("-" * 20)
Primeiro = int(input("Digite o primeiro termo: "))
print("-" * 20)
Razao = int(input("Digite a razão: "))
n = 1
termo = Primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while n <= total:
        termo = termo + Razao
        print('{}  - '.format(termo), end='')
        n += 1
    print("Pausa")
    mais = int(input("Quantos termo a mais você quer?: "))


