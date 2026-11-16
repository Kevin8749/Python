Nums = []
Record = 0
Record_Menor = 0

for num in range(0,5):
    Read = int(input("Digite os valores: "))
    Nums.append(Read)
    if num == 0:
        Record = Read
        Record_Menor = Read
    else:
        if Read > Record:
            Record = Read
        if Read < Record_Menor:
            Record_Menor = Read
print(f"O maior número é: {Record} nas posições ", end='')
for i, v in enumerate(Nums):
    if v == Record:
        print(f"{i}...", end='')
print()
print(f"O maior número é: {Record_Menor} nas posições ", end='')
for k,o in enumerate(Nums):
    if o == Record_Menor:
        print(f"{k}...", end='')
print()



