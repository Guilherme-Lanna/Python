num = int(input('Diga um número: '))
print('Tabela de conversão:\n'
      '     1 para binário\n'
      '     2 para octal\n'
      '     3 para hexadecimal')
base = int(input('Qual a conversão desejada? '))
if base == 1:
    print('O número {} em binário é igual a {}'.format(num,bin(num)[2:]))
elif base == 2:
    print('O número {} em octal é igual a {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('O número {} em hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Escolha inválida!!')