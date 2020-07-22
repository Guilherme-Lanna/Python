valor = float(input('Qual o valor do produto? R$'))
print('-=-'*20)
print('Formas de pagamento:\n'
      '--> À vista no dinheiro ou cheque - digite \033[1;32m1\033[m\n'
      '--> 1x no cartão - digite \033[1;32m2\033[m\n'
      '--> 2x no cartão - digite \033[1;32m3\033[m\n'
      '--> 3x ou mais no cartão - digite \033[1;32m4\033[m\n')
print('-=-'*20)
pagar = int(input('Qual a forma de pagamento escolhida? '))
des10 = valor * (10/100)
des5 = valor * (5/100)
juros = valor * (20/100)
if pagar == 1:
    print('Você receberá um desconto de 10%, o novo valor do produto será R${}!'.format(valor - des10))
elif pagar == 2:
    print('Você receberá um desconto de 5%, o novo valor do produto será de R${}!'.format(valor - des5))
elif pagar == 3:
    print('A forma de pagamento escolhida foi dividir 2x no cartão, e será pago o valor normal do produto, R${}!'.format(valor))
elif pagar == 4:
    print('Será aplicado um juros de 20%, ocasionando no novo valor do produto igual a R${}'.format(valor + juros))