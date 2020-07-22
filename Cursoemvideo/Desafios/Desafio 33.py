n1 = float(input('Primeiro valor - '))
n2 = float(input('Segundo valor - '))
n3 = float(input('Terceiro valor - '))
if n1 > n2 > n3:
    print('O número {} é o maior número e o número {} é o menor numero'.format(n1, n3))
if n1 > n3 > n2:
    print('O número {} é o maior número e o número {} é o menor numero'.format(n1,n2))
if n3 > n2 > n1:
    print('O número {} é o maior número e o número {} é o menor numero'.format(n3,n1))
if n2 > n1 > n3:
    print('O número {} é o maior número e o número {} é o menor numero'.format(n2, n3))
if n2 > n3 > n1:
    print('O número {} é o maior número e o número {} é o menor numero'.format(n2, n1))
if n3 > n1 > n2:
    print('O número {} é o maior número e o número {} é o menor numero'.format(n3, n2))