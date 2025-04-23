'''
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite outro número: "))
n4 = int(input("Digite outro número: "))
n5 = int(input("Digite o último número: "))

print(f"A SOMA dos números é {n1+n2+n3+n4+n5}\n A MÉDIA dos números é {(n1+n2+n3+n4+n5)/5}")'''

#Professor
soma = 0
i = 0
while i < 5:
    num = input(f"Diga o {i+1} número: ")
    while not num.isnumeric():
        num = input(f"Diga o {i+1} número: ")
    num = int(num)
    soma += num
    i += 1
media = soma/i
print(media)