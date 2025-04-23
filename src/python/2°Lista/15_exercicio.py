#professor
#Não terminei de copiar

candidato_1 = 0
candidato_2 = 0
candidato_3 = 0
candidato_4 = 0
brancos = 0
nulos = 0

while True:
    num = input("1- João, 2- Danilo, 3- Marta, 4-  Neymar, 5- Brancos, 6- Nulos ")
    while not num.isnumeric():
        print("Inválido")
        num = input("Digite um número: ")
    num = int(num)
    if num < 1:
        candidato_1 += 1
    elif num < 2:
        candidato_2 += 1
    elif num < 3:
        candidato_3 += 1
    elif num < 4:
        candidato_4 += 1
    elif num < 5:
        brancos += 1
    elif num < 6:
        nulos += 1

    else:
        print("Invalido")
    continuar = input("Voce quer conitnuar? (s/n)\n ->")
    while not (continuar =='s' or continuar == 'n'):
        print("Invalido")
        continuar = input("Voce quer conitnuar? (s/n)\n ->")
    if continuar =='n':
        break
total = 0
print(f"João - {candidato_1} votos\n Danilo - {candidato_2} votos\n Marta - {candidato_3}\n Neymar - {candidato_4} votos\n Brancos - {brancos} votos\n Nulos - {nulos} votos")
print(f'A porcentagem de votos brancos e nulos sobre o total é de')