# 1. Função que recebe os dados e faz a verificação
def verificar_entrada(com_pais, adulto, ingresso):
    # Usamos parênteses para garantir a ordem da lógica (E / OU)
    if (com_pais or adulto) and ingresso:
        print("Pode passar! Seja bem-vindo(a).")
    else:
        print("Você não pode passar (falta de ingresso, acompanhante ou idade).")

# 2. Coletando os dados do usuário (convertendo para minúsculas para facilitar a comparação)
pais_input = input("Você está com os pais? (Sim/Não): ").strip().lower()
adulto_input = input("Você é um adulto? (Sim/Não): ").strip().lower()
ingresso_input = input("Você tem um ingresso? (Sim/Não): ").strip().lower()

# 3. Transformando as respostas em valores Verdadeiro (True) ou Falso (False)
esta_com_pais = (pais_input == "sim")
e_adulto = (adulto_input == "sim")
tem_ingresso = (ingresso_input == "sim")

# 4. Chamando a função com os valores corretos
verificar_entrada(esta_com_pais, e_adulto, tem_ingresso)