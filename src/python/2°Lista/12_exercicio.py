nota = input("Digite break para parar o programa e calcular a média\nDigite a nota do aluno: ")
N = 0
a = 0

while not (nota == 'break'):
    if nota.isnumeric():
        a = a + int(nota)
        N = N + 1
        nota = input("Digite break para calcular média\nDigite a nota do aluno: ")

print(f"A média do aluno é {a/N: .2f}")