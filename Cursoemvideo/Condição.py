nome = str(input('Qual o seu nome? ')).strip()
if nome.upper() == 'GUILHERME':
    print('Que nome interessante!')
else:
    print('Legal!')
print('Bom dia, {}'.format(nome))


n1 = float(input('\nQual foi sua nota do 1º bimestre, {}? '.format(nome)))
n2 = float(input('Qual foi a sua nota do 2º bimestre? '))
n3 = float(input('Qual foi a sua nota do 3º bimestre? '))
n4 = float(input('Qual foi a sua nota do 4º bimestre? '))
media = (n1+n2+n3+n4)/4
if media >= 5:
    print('\nParabéns {}, você passou de ano!'.format(nome))
else:
    print('\nQue pena {}, você está de recuperação!'.format(nome))
