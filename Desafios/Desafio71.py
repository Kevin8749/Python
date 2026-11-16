print("=" * 20)
print("Banco Devex")
print("=" * 20)

Saque = int(input("Que valor você quer sacar? R$ "))
Estoque = [50,20,10,1]
i = 0
while True:
    cédulas = Estoque[i]
    Total_Cédulas = Saque // cédulas 
    Saque = Saque % cédulas
    
    if Saque == 0 and  i <= len(Estoque):
        break
    if Saque > 0:
        print(f"O total de cédulas: {Total_Cédulas} de: {cédulas}")
    i += 1
print(f"O total de cédulas: {Total_Cédulas} de: {cédulas}")

