s = float(input('Qual o seu salário atual? R$'))
a10 = s * (10/100)
a15 = s * (15/100)
if s >= 1250:
    print('Você receberá um aumento de 10%, seu novo salário será de R${:.2f}'.format(s+a10))
else:
    print('Você receberá um aumento de 15%, seu novo salário derá de R${:.2f}'.format(s+a15))