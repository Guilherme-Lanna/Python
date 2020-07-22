print('-=-' * 40)
print('Diga-me três tamanhos de retas para saber se com essas retas se pode formar um triângulo.')
print('-=-' * 40)
l1 = float(input('Lado 1 = '))
l2 = float(input('Lado 2 = '))
l3 = float(input('Lado 3 = '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('-' * 40)
    print('É possível formar um triângulo com essas medidas!')
    print('-' * 40)
else:
    print('-' * 40)
    print('Não é possível formar um triângulo com essas medidas!')
    print('-' * 40)

if l1 == l2 == l3:
    print('Será formado um triângulo EQUILÁTERO!')
elif l1 == l2 or l1 == l3 or l2 == l3:
    print('Será formado um triângulo ISÓSCELES!')
else:
    print('Será formado um triângulo ESCALENO!')