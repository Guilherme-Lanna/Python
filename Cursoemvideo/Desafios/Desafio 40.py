print('Vamos ver como você está na escola!')
nota1 = float(input('Me diga sua nota do 1º semestre: '))
nota2 = float(input('E a sua nota do 2º semestre: '))
media = (nota1 + nota2)/2
if media <= 5:
    print('Sua média foi {:.1f}, você está reprovado!'.format(media))
elif media > 5 and media < 6.9:
    print('Sua média foi {:.1f}, você está de recperação!'.format(media))
elif media >= 7:
    print('Sua média foi {:.1f}, você foi aprovado!!'.format(media))