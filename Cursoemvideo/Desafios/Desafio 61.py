
num1 = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
cont = 0
termo = num1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += raz
    cont += 1
print('FIM!')
