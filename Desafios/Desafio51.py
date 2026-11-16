print("=" * 20)
print("Primeiro termo de razão(10)")
print("=" * 20)
Valor = int(input("Primeiro termo:\n"))
Razao = int(input("Razao:\n"))
Décimo_Termo = Valor + (10 - 1) * Razao
for con in range(Valor,Décimo_Termo + 1,Razao):
      print(con)
print("Acabou")