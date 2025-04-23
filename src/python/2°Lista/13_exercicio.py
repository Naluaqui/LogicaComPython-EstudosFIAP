#professor: Crescimento exponencial
salario = 1000
taxa = 1.5/100
ano = 1995

while ano < 2025:
    salario *= 1 + taxa
    taxa *= 2       #A taxa dobra
    ano += 1        #Passou um ano

print(salario)