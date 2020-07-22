#from math import sqrt
#co = float(input('Qual o tamanho do cateto oposto do triangulo retangulo ? '))
#ca = float(input('Qual o tamanho do cateto adjascente do triangulo retangulo ? '))
#h = (ca**2)+(co**2)
#resul = sqrt(h)
#print('O valor da hipotenusa do triangulo retangulo é igual a {:.2f}'.format(resul))

import math
co = float(input('Qual o tamanho do cateto oposto do triangulo retangulo ? '))
ca = float(input('Qual o tamanho do cateto adjascente do triangulo retangulo ? '))
h = math.hypot(co , ca)
print('O valor da hipotenusa do triangulo retangulo é igual a {:.2f}'.format(h))

