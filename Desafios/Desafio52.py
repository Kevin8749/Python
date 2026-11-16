number = int(input("Digite um número limite:\n"))
soma = 0

# Passamos por cada número 'n' desde 2 até o número digitado
for n in range(1, number + 1):
     if number % n == 0:
         print(f"\033[1;32;40m {n} \033[m")
         soma += 1
     else:
          print(f"\033[1;31;40m {n} \033[m")
if soma >= 3:
     print(f"ESSE NÚMERO {number} não é primo!")
elif number > 1:
     print(f"Esse número {number} é primo") 
else:
     print(f"ESSE NÚMERO {number} não é primo!")
    