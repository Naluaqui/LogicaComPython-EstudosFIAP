nome = input("Qual é o seu nome?")
while not len(nome)>=3:
    nome = input("Qual é o seu nome?")

idade = int(input("Quantos anos você tem?"))
while not (idade>=0 and idade<=150):
    idade = int(input("Quantos anos você tem?"))

salario = float(input("Qual é o seu salário?"))
while not (salario>0):
    salario = float(input("Qual é o seu salário?"))

sexo = input("Qual é seu sexo?")
while not (sexo=='f' or sexo=='m'):
    sexo = input("Qual é seu sexo?\n f = feminino\n m = masculino")

civil = input("Qual é seu estado civil?")
while not (civil=='s' or civil =='c' or civil== 'v' or civil=='d'):
    civil = input("Qual é seu estado civil?\n s para solteiro\n c para casado\n v para viuvo\n d para divorciado")

print(f"Então, o seu nome é {nome}\n Você tem {idade} anos\n O seu salário é R${salario}\n O seu estado civil é {civil}")