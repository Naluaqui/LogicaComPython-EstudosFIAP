'''
nota = int(input("Digite a nota do aluno:"))
vezes = 0
while not (nota<=10):
    nota = int(input("Digite a nota do aluno:"))'''

#VERSAO DO PROF

while True:
    nota = input("Diga sua nota: ")
    if nota.isnumeric ():
        nota = int(nota)
        if nota > 0 and nota < 10:
            break