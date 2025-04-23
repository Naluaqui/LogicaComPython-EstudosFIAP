#professor

fatorial = 1
num = 5
i = 1
produto = f'{num}!= '
while i <= num:
    fatorial *= i
    if i < num:
        produto += f'{num - i + 1}*'
    else:
        produto += f'{num - i +1} = {fatorial}'
    i += 1
print(produto)