from datetime import date
ano = int(input('Diga o ano em que deseja descobrir se é bissexto ou não (para o ano atual, digite 0): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('O ano de {} é um ano bissexto!'.format(ano))
else:
    print('O ano de {} não é um ano bissexto'.format(ano))