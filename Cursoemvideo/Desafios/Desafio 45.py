from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:'
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 } TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('-=-' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador escolheu {}'.format(itens[jogador]))
print('-=-' * 11)
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('EMPATE!!')
    elif jogador == 1:
        print('PARABÉNS!!, Você venceu!')
    elif jogador == 2:
        print('Você PERDEU!!')
    else:
        print('JOGADA INVÁLIDA!!')
elif computador == 1:  # computador jogou papel
    if jogador == 0:
        print('Você PERDEU!!')
    elif jogador == 1:
        print('EMPATE!!')
    elif jogador == 2:
        print('PARABÉNS, Você venceu!')
    else:
        print('JOGADA INVÁLIDA!!!')
elif computador == 2:  # computador jogou tesoura
    if jogador == 0:
        print('PARABÉNS, Você venceu!!')
    elif jogador == 1:
        print('Você PERDEU!!')
    elif jogador == 2:
        print('EMPATOU!!')
    else:
        print('JOGADA INVÁLIDA!!!')