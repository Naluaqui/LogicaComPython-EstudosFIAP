lista = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k']
for i in range(len(lista)):
    if i%2 ==0:
        print(lista[i])
vogais = 0
for char in lista:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        vogais += 1

'''Essa forma é mais indica pois o indice (i) é importante, não podemos perder o local das coisas'''
#Acessando a lista -> lista[i]

vogais = 0
for i in range (len(lista)):
    print(f'Vou verificar se lista[{i}], ou seja, {lista[i]} é vogal')
    if lista [i] == 'a' or lista [i] == 'e' or lista [i] == 'i' or lista [i] == 'o' or lista [i] == 'u':
       print('sim')
        vogais += 1
        continue
    print('não')

#por elementos
numeros = [3,2,7,1,8,9]
soma = 0
for i in range(len(numeros)):
   soma += numeros[i]
   print(soma)