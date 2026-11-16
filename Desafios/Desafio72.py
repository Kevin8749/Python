Nums = ("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quartoze","quinze","dezeseis","dezesete","dezoito","dezenove","vinte")
Escolha = int(input("Digite um numero entre 0 a 20: "))
if Escolha > 20 or Escolha < 0:
    print("Número inválido")
else:
    print(Nums[Escolha])

