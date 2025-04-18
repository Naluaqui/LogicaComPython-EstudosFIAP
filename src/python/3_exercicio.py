a = 80000
b = 200000
ano = 0

while not (a>=b):
    a = (a*3/100) + a
    b = (b*1.5/100) + b
    ano = ano + 1

print(f"Em {ano} anos, o país A vai ter {a: .2f} habitantes e o país B {b: .2f} habitantes.")

if a>b:
    print(f"O país A tem {a-b: .2f} habitantes a mais")
else:
    print(f"O país B tem {b-a: .2f} habitantes a mais")