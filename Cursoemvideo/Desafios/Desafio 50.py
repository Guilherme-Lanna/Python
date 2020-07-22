soma = 0
cont = 0
for i in range(0, 6):
    num = int(input('Digite o {}º número: '.format(i + 1)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números,\n'
      'A soma dos numeros pares entre 0 e 6 é igual a {}'.format(cont, soma))