v = int(input('Velocidade do carro ao passar no radar = '))
m = v-80
if v > 80:
    print('O carro estava acima da velocidade permitida')
    print('A multa irá custar R${}'.format(m*7))
