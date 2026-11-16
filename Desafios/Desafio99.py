from time import sleep
def maior(*nums):
    print("-=" * 30)
    print("Analisando os valores passados...")
    for valor in nums:
        print(f"{valor}", end =" ", flush=True)
        sleep(0.40)
    if valor == "":
        print("Foram informados 0 valores ao todo")
        print("O maior valor informado foi 0")
    else:
        print(f"Foram informados {len(nums)} valores ao todo")
        print(f"O maior valor informado foi {max(nums)}")

maior(5,2,2,3,32,3,21,5,5)
maior(4,7,0)
maior(1,2)
maior("")