'''

n1 = int(input("Digite o pimeiro número: "))
n2 = int(input("Digite o pimeiro número: "))
n3 = int(input("Digite o pimeiro número: "))
n4 = int(input("Digite o pimeiro número: "))
n5 = int(input("Digite o pimeiro número: "))
n6 = int(input("Digite o pimeiro número: "))
n7 = int(input("Digite o pimeiro número: "))
n8 = int(input("Digite o pimeiro número: "))
n9 = int(input("Digite o pimeiro número: "))
n10 = int(input("Digite o pimeiro número: "))

par = 0
impar = 0

if n1 % 2 == 0:
    par = par + 1
else:
    impar = impar + 1

if n2 % 2 == 0:
    par = par + 1
else:
    impar = impar + 1

if n3 % 2 == 0:
    par = par + 1
else:
    impar = impar + 1

if n4 % 2 == 0:
    par = par + 1
else:
    impar = impar + 1

if n5 % 2 == 0:
    par = par + 1
else:
    impar = impar + 1

if n6 % 2 == 0:
    par = par + 1
else:
    impar = impar + 1

if n7 % 2 == 0:
    par = par + 1
else:
    impar = impar + 1

if n8 % 2 == 0:
    par = par + 1
else:
   
    impar = impar + 1

if n9 % 2 == 0:
    par = par + 1
else:
    impar = impar + 1

if n10 % 2 == 0:
    par = par + 1
else:
    impar = impar + 1

print(f"Quantidade de números pares {par}\nQuantidade de números ímpares {impar}")'''

#Professor
i = 0
pares = 0 #não declarei direito, talvez o codigo não funcione mas é tipo isso
while i < 10:
    num = input(f"Diga o {i+1} número: ")
    while not num.isnumeric():
        num = input(f"Diga o {i + 1} número: ")
    num = int(num)
    if num%2 == 0:
        pares += 1
    i += 1
print(f"Você digitou {pares} pares e {i - pares} ímpares.")