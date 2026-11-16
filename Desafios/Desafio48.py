soma = 0
cont = 0
for Imapar in range(1,500,1):
    if Imapar % 2 != 0:
       if Imapar % 3 == 0:
          cont += 1
          soma += Imapar
print(f"A soma de {cont} é  {soma}")