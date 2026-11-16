n1 = int(input("Digite o primeiro número:\n"))
n2 = int(input("Digite o segundo número:\n"))
n3 = int(input("Digite o terceiro número:\n"))

if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n1 and n2 >= n3:
    maior = n2
else:
    maior = n3

if n1 <= n2 and n1 <= n3:
    menor = n1
elif n2 <= n1 and n2 <= n3:
    menor = n2
else:
    menor = n3

if n1 == n2 or n1 == n3 or n2 == n3:
    print("Há números empatados.")
 

print(f"O maior número é: {maior} e o menor número é: {menor}")