opcoes = ['Cola Cola', 'Pepsi', 'Guaraná', 'Cervejinha', 'Caipirinha']
escolha = input('Qual bebida voc}e quer?\n->')
while not escolha in opcoes:
    escolha = input('Qual bebida voc}e quer?\n->')


#FUNÇÃO

def forca_opcao(msg,lista_opcoes):
    opcoes = '\n' .join(lista_opcoes)
    escolha = input(f'{msg}\n{opcoes}\n->')
    while not escolha in lista_opcoes:
        escolha = input(msg)
    return escolha

opcoes = ['Cola Cola', 'Pepsi', 'Guaraná', 'Cervejinha', 'Caipirinha']
opcao = forca_opcao( "Qual bebida você quer?\n->", opcoes)
print(f'Você escolheu {opcao}')
opcoes_2 = ['sim', 'nao']
opcao = forca_opcao( 'dIGA SIM OU NÃO', opcoes_2)
print(f'Você escolheu {opcao}')



#Exemplo
opcoes = ['lilith', 'Pandora', 'Pepita']
frase = ''
sep = '🐱‍🐉'
for palavra in opcoes:
    frase += sep+palavra
print(frase)

#MELHORADO

opcoes = ['lilith', 'Pandora', 'Pepita']
frase = opcoes[0]
for i in range(1,len(opcoes)):
    frase += sep + opcoes[i]
print(frase)

#funcao
def join(lista_str,sep):
    frase = lista_str[0]
    sep = '🐱‍🐉'
    for i in range(1,len(lista_str)):
        frase += sep + lista_str[i]
    return frase

def forca_opcao(msg,lista_opcoes):
    #opcoes = '\n' .join(lista_opcoes)
    opcoes = join(lista_opcoes, '🐱‍🐉')
    escolha = input(f'{msg}\n{opcoes}\n->')
    while not escolha in lista_opcoes:
        escolha = input(msg)
    return escolha

opcoes = ['lilith', 'Pandora', 'Pepita']
escolha = forca_opcao('Escolha um dog para salvar do jacaré:',opcoes)


#Inverter

a = [1,2,3,4,5,6,7]
i = 0

for i in range(len(a)//2):
    aux = a[i]
    a[i] = a[len(a)-1-i]
    a[len(a)-1-i] = aux
    i += 1

#função inverter 

def inverter_lista(lista):
    i = 0
    for i in range(len(a)//2):
        aux = a[i]
        a[i] = a[len(a)-1-i]
        a[len(a)-1-i] = aux
        i += 1
    return

a = [1,2,3,4,5,6,7,8,9,10,11]
inverter_lista(a)
print(a)