maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input('Qual o peso da {}ª pessoa? '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O maior peso lido foi {}Kg,'.format(maior))
print('E o menor peso lido foi {}Kg'.format(menor))


