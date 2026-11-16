def Area(largura,comprimento):
    area = largura * comprimento
    print(f"A area de um terreno {largura}x{comprimento} é de {area}m")
print("Controle de Terrenos")
print("_" * 15)
Largura = float(input("LARGURA (m): "))
Comprimento = float(input("COMRPIMENTO (m):"))
Area(Largura, Comprimento)