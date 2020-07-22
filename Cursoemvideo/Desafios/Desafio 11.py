h = float(input('Qual a altura da parede que será pintada?'))
l = float(input('E a largura desta?'))
a = h * l
t = 2
p = a / t
print('Sabendo que a parede tem {} m², e que cada litro de tinta tem a capacidade de cobrir {} m², será preciso {} l de tinta!!'.format(a, t, p))