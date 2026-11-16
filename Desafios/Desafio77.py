Palavras = "programador", "amador", "python"

for Palavra in Palavras:
    print(f"\n Na palavra {Palavra} temos ", end="")
    for vogal in Palavra:
        if vogal in "aeiou":
            print(vogal, end=" ")

    