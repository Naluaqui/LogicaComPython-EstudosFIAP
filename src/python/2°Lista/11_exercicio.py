#professor: número primo lógica

num = 35
i = 2
while i < num:
    print(f'{num}%{i} = {num%i}')
    if num %1 == 0:
        print(f'{num} não é número primo!')  #Esse código é uma merda porque é redondante
        break
    elif i == num - 1:
        print(f'{num} é primo')

'''
num = 37
i = 2
while i < num:
    print(f'{num}%{i} = {num%i}')
    if num %1 == 0:
        print(f'{num} não é número primo!')
        break
    elif i >= num**(0.5):               #Raiz quadrada de X é X², ou seja MEIO
        print(f'{num} é primo')
        break
    i += 1
'''