N = int(input())
for n in range(N):
    frase_em_lista = []
    string = input()
    strings_separadas = list(string.split(" "))

    for strings in strings_separadas:
        for x, e in enumerate(strings):
            if x == 0:
                frase_em_lista.append(e[0])

    frase_formada = ''.join(frase_em_lista)
    print(frase_formada)