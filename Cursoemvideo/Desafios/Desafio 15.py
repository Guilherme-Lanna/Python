kmrd = float(input('Quantos quilometros o carro rodou?'))
diard = int(input('Quantos dias você ficou com o carro?'))
vkm = 0.15
vdia = 60
total = (kmrd * vkm) + (diard * vdia)
print('O total a pagar é de R${}'.format(total))