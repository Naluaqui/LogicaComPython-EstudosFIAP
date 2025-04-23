'''
n1 = int(input("Diga um número inteiro: "))
n2 = int(input("Diga outro número inteiro: "))
print(list(range(n1, n2)))'''

#Professor

a = input("Diga um numero: ")
while not a.isnumeric():
    a = input("Diga um numero: ")
a = int(a)

b = input("Diga um numero: ")
while not b.isnumeric():
    b = input("Diga um numero: ")
b = int(b)

if a> b:
    aux = a
    a = b
    b = aux

while a <= b:
    print(a, end=' ') #O espaço aqui é necessário
    a += 1