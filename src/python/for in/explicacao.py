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

#pareando listas
media_final = [7,2,3,6,4]
alunos = ['Luís', 'João', 'Ana Luiza', 'José', 'Sofia']
for i in range (len(media_final)):
    if media_final[i] >= 6:
        print(f'O/A {alunos[i]} passou')

profs = ['Celso', 'Demetrius', 'Aurelio', 'Ana', 'Cidade', 'Luís', 'Danilo']
materias = ['Cálculo', 'Edge', 'Sw&TX', 'Story', 'Front', 'Web', 'Python']
for i in range (len(profs)):
    if profs[i] == 'Danilo':
        print(f'O {profs[i]} é o melhor professor 💕😁👍')


#exercicio
profs = ['Celso', 'Demetrius', 'Aurelio', 'Ana', 'Cidade', 'Luís', 'Danilo']
materias = ['Cálculo', 'Edge', 'Sw&TX', 'Story', 'Front', 'Web', 'Python']
for i in range(len(profs)):
    print(f'O professor(a) {profs[i]} ensina {materias[i]}')


#Algoritmos das setas
numeros = [2,5,3,6,7,1,4]
maior = 2 #A seta em formato de código
for num in numeros:
    print(f'Vou testar se {num} é maior que {maior}')
    if num > maior:
        print(f'Deu certo, vou trocar {maior} por num')
        maior = num