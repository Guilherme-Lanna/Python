

num1 = float(input('Digite um valor: '))
num2 = float(input('Digite outro valor: '))
escolha = 0
while escolha != 5:
    print('''[1] Soma
          [2] Multiplicação
          [3] Maior dos números
          [4] Escolher novos números
          [5] Sair do programa''')
    escolha = int(input('>>>>Qual a opção desejada? '))
    if escolha == 1:
        print('A soma dos dois números é igual a {}'.format(num1 + num2))
    if escolha == 2:
        print('A multiplicação dos dois números é igual a {}'.format(num1 * num2))
    if escolha == 3:
        if num1 > num2:
            print('Entre {} e {}, o número maior é {}'.format(num1,num2, num1))
        else:
            print('Entre {} e {}, o número maior é {}'.format(num1, num2,num2))
    if escolha == 4:

        num1 = float(input('Digite um valor: '))
        num2 = float(input('Digite outro valor: '))
    if escolha == 5:
        print('Finalizando...')
    print('-==-' * 20)
print('Fim!')