n = int(input('Digite um numero: '))
opt = str(input('Quer continuar ? [S/N]: ')).upper()
soma = n
media = 0
count = 1
maior = n
menor = n


while opt not in 'Nn':
    if opt not in 'Ss':
        print('Opcao Invalida!')
        opt = str(input('Quer continuar? [S/N]: ')).upper()
    else:
        count += 1
        n = int(input('Digite um numero: '))
        soma += n
        if n < menor:
            menor = n
        if n > maior:
            maior = n
        opt = str(input('Quer continuar? [S/N]')).upper()