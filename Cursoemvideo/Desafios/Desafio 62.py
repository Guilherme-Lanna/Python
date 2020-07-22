num1 = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
c = 10
while c > 0:
    print('{} -> '.format(num1), end=' ')
    num1 += raz
    c -= 1
    if c == 0:
        c = int(input('\nAcrescentar mais números na sequência: '))
print('FIM!')