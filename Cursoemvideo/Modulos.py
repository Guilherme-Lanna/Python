#import math
#num = int(input('Digite um número:'))
#raiz = math.sqrt(num)
#print('A raiz quadrada do numero {} é igual a {}'.format(num, raiz))
#print('A raiz quadrada do numero {} é igual a {}'.format(num, math.ceil(raiz)))
#print('A raiz quadrada do numero {} é igual a {}'.format(num, math.floor(raiz)))

#from math import sqrt
#num = int(input('Dgite um numero:'))
#raiz = sqrt(num)
#print('A raiz quadrada do numero {} é igual a {}'.format(num, raiz))

from math import sqrt, floor
num = int(input('Dgite um numero:'))
raiz = sqrt(num)
print('A raiz quadrada do numero {} é igual a {}'.format(num, floor(raiz)))


import random
num = random.randint(1,10)
print('Um numero aleatorio' ,num)
