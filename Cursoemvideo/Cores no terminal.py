print('\033[4;30;45m Olá, mundo!\033[m')

print('\n\033[7;30mOlá, tudo bem?\033[m')

a = 3
b = 5
print('\n\033[1mOs valores são igual \033[1;32m{}\033[m \033[1me \033[1;36m{}\033[m!!!'.format(a,b))

nome = 'Guilherme'
cores = {'limpa':'\033[m',
         'negrito':'\033[1m',
         'azul': '\033[1;36m',
         'amarelo':'\033[1;32m',
         'bw':'\033[7;30m'}
print('{}Olá muito prazer {}{}{}{}'.format(cores['negrito'],cores['limpa'], cores['azul'], nome, cores['limpa']))