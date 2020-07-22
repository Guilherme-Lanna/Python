import random
print('-=-' * 40)
print('Vou pensar em um número de 0 a 5, tente adivinhar em que número eu pensei.')
print('-=-' * 40)
r = random.randint(0,5)
num = int(input('Adivinhe o numero escolhido: '))
if num == r:
    print('-' * 40)
    print('Parabéns, o número esolhido é o numero {}'.format(num))
    print('-' * 40)
else:
    print('-' * 40)
    print('ERRADO, o número escolhido foi o número {}'.format(r))
    print('-' * 40)