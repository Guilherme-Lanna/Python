n1 = int(input("DIgite um número ="))
n2 = int(input("Digite outro número ="))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print("A soma dos dois números é {}, \n a multiplicação entre esses é {}, \n já a divisão é {:.3f}".format(s, m, d), end=' --- ')
print('A divisão inteira {}, \n a potencialização entre esses numeros é igual a {}.'.format(di, e))