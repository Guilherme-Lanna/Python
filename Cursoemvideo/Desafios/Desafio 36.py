casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu saláro atual? R$'))
anos = int(input('Em quantos anos pretende pagar a casa? '))
meses = anos * 12
prest = casa / meses
maximo = salario * (30/100)
print('-=-'*35)
print('Você terá que pagar R${:.2f} por mês durante {} anos'.format(prest, anos))
if prest > maximo:
    print('Porém, infelizmente você não poderá financiar esta casa')
else:
    print('E esta casa está dentro do seu orçamento!')