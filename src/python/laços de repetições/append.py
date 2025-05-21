qtd = input('Quantos números você vai colocar?\n->')
while not qtd.isnumeric():
    qtd = input('Quantos números você vai colocar?\n->')
qtd = int(qtd)

numeros  = []
while len(numeros) < qtd:
    num = input(f'Diga o {len(numeros)+1}° número:')
    while not num.isnumeric():
        num = input(f'Diga o {len(numeros) + 1}° número:')
    num = int(num)
    numeros.append(num)