print('\033[1;35m-=-\033[m'*10)
print('Vamos medir seu IMC!')
print('\033[1;35m-=-\033[m'*10)
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura*altura)
if imc <= 18.5:
    print('Seu IMC é igual a {:.1f} e você está abaixo do peso!'.format(imc))
elif imc > 18.5 and imc <= 25:
    print('Seu IMC é igual a {:.1f} e você está no peso ideal!'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu IMC é igual a {:.1f} e você está com sobrepeso!'.format(imc))
elif imc > 30 and imc <= 40:
    print('Seu IMC é igual a {:.1f} e você está com obesidade!')
elif imc > 40:
    print('Seu imc é igual a {:.1f} e você esta com obesidade morbida!')