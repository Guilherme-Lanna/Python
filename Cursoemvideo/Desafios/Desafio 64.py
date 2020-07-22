n = c = soma = 0
while n != 999:
    n = int(input('Digite o número inteiro: '))
    if n != 999:
        c += 1
        soma = soma + n
print('Foram digitados {} valores e a soma deles é {}.'.format(c, soma))