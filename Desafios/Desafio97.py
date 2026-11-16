def escrever(text: str):
    text_new = text.replace(" ", "")
    Total = len(text_new) + 5
    print("~" * Total)
    print(f"  {text}")
    print("~" * Total)
escrever("Gustavo Guanabara")
escrever("Curso de Python no Youtube")
escrever("CeV")
