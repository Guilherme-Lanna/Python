from datetime import date
print('Me de algumas informações para eu saber sobre seu alistamento militar!')
atual = date.today().year
ano = int(input('Qual o seu ano de nascimento? '))
idade = atual - ano
if idade < 18:
    print('Você deve se alistar daqui {} anos'.format(18-idade))
elif idade == 18:
    print('Está na hora de você realizar seu alistamento')
elif idade > 18:
    print('Você deveria ter se alistado a {} anos atras'.format(idade-18))