n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
result = n1 +  n2 # Se não usar o int, o resultado será uma concatenação de strings
print(f"A soma de {n1} + {n2} é igual a {result}")
# -- 
read = input("Precione qual quer tecla"  )

print(f"Tipo da variável: {type(read)}")# Mostra o tipo da variável
print(f"É alfabética? {read.isalpha()}") # Mostra se a variável é alfabética
print(f"É numérica? {read.isnumeric()}") # Mostra se a variável é numérica
print(f"É alfanumérica? {read.isalnum()}") # Mostra se a variável é alfanumérica
print(f"É maiúscula? {read.isupper()}") # Mostra se a variável é maiúscula