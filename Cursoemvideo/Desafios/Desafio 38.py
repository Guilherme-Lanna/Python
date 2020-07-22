print('\033[34mMe diga dois números para que possamos compara-los!\033[m')
n1 = float(input('Número 1 = '))
n2 = float(input('Número 2 = '))
if n1 > n2:
    print('O primeiro valor, \033[32m{}\033[m,  é maior!'.format(n1))
elif n2 > n1:
    print('O segundo valor,\033[32m{}\033[m, é maior!'.format(n2))
else:
    print('Os dois números tem o mesmo valor!')