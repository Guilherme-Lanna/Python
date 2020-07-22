import random
print('-=-' * 40)
print('Vou pensar em um número de 0 a 1, tente adivinhar em que número eu pensei.')
print('-=-' * 40)
r = random.randint(0,10)
num = 11
cont = 0
while num != r:
    num = int(input('Qual seu palpite? '))
    if num > r:
        print('Menos... Tente novamente!')
    if num < r:
        print('Mais... Tente novamente')
    cont += 1
if num == r:
    print('Parabéns você acertou na {}ª tentativa'.format(cont))
