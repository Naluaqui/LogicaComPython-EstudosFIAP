#professor
#vai ser importante para a prova

while True:
    num = input("Digite um número: ")
    while not num.isnumeric():
        print("Inválido")
        num = input("Digite um número: ")
    num = int(num)
    if num < 25:
        intervalo_1 += 1
    elif num < 50:
        intervalo_2 += 1
    elif num < 75:
        intervalo_3 += 1
    elif num < 100:
        intervalo_4 += 1
    else:
        print("Invalido")
        continuar = input("Voce quer conitnuar? (s/n)\n ->")
        while not (continuar =='s' or continuar == 'n'):
            print("Invalido")
            continuar = input("Voce quer conitnuar? (s/n)\n ->")
        if continuar =='n':
            break