plv = input("Digite a palavra a procurar: ")
name = input("Digite o nome do ficheiro: ")
with open(f'{name}.txt', 'r', encoding='utf-8') as f:
    for linha in f:
        if plv in linha:
            print(linha.strip())