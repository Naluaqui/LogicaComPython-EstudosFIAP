'''
num = int(input("Digite o número que tu quer saber a tabuada: "))
print(f"{num} X 1 = {num*1}\n{num} X 2 = {num*2}\n{num} X 3 = {num*3}\n{num} X 4 = {num*4}\n{num} X 5 = {num*5}\n{num} X 6 = {num*6}\n{num} X 7 = {num*7}\n{num} X 8 = {num*8}\n{num} X 9 = {num*9}\n{num} X 10 = {num*10}")'''

#professor
'''
num = 3
mult = 1
while mult <= 10:
    print(f"{mult}*{num} = {mult*num}")
    mult += 1
'''

#Professor deixou o exercici mais fofo

num = 1
while num <=10:
    mult = 1 #resetando o mult
    print(f"Tabuada do {num}: ")
    while mult <= 10:
        print(f"{mult}*{num} = {mult*num}")
        mult += 1
    print() #espaço
    num += 1