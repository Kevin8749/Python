frase = str(input("Escreva uma frase e eu direi se ela é palíndromo:\n")).upper()

# 1. Tira os espaços da frase
frase_limpa = frase.replace(" ", "")

# 2. Cria uma variável vazia para guardar a frase invertida
frase_invertida = ""

# 3. Pega o tamanho total da frase limpa
tamanho = len(frase_limpa)

# 4. Loop que vai de trás para frente (do último índice até o 0)
# Lembre-se: no Python, os índices vão de 0 até (tamanho - 1)
for i in range(tamanho - 1, -1, -1):
  frase_invertida = frase_invertida + frase_limpa[i]

# 5. Compara a frase limpa com a invertida
print(f"Sua frase {frase} ficou assim {frase_invertida}")
if frase_limpa == frase_invertida:
  print(f"Sim! '{frase}' é um palíndromo!")
else:
  print(f"Não, '{frase}' não é um palíndromo.")