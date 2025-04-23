#Professor

a = 1
b = 1
i = 0
print(a,b,end=' ')
while i < 10:
 c = a + b
 a = b
 b = c
 i += 1
 print(c,end = ' ')