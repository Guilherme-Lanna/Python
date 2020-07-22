from datetime import datetime
a = datetime.now()
n = 0
n1 = 0
for c in range(7):
    a1 = int(input('Ano de nascimento: '))
    if (a.year) - a1 >= 21:
        n = n + 1
    elif (a.year) - a1 < 21:
        n1 = n1 + 1
print('{} pessoas são maiores de 18\n'
      '{} pessoas são menores de 18'.format(n, n1))