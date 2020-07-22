
num = int(input("Digite um número para seu fatorial ser calculado: "))
m = num
fat = 1
print('Calculando {}! =  '.format(num), end='')
while m > 0:
    print(' {} '.format(m), end='')
    print(' x ' if m > 1 else ' = ', end='')
    fat *= m
    m -= 1
print('{}'.format(fat))