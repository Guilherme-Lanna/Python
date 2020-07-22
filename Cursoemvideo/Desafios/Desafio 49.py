num = int(input('Encolha a tabuada que deja consultar: '))
for i in range(0, 11):
    print('{} x {} = {}'.format(num, i, num*i))