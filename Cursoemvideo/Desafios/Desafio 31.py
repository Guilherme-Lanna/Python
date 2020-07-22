dis = float(input('Qual a distância da viagem: '))
vpq = dis * 0.50
vlg = dis * 0.45
if dis < 200:
    print('A viagem tem o valor de R$0,50 por kilometro,\n'
          'sendo assim sua viagem ficou no valor de {:.2f}'.format(vpq))
else:
    print('A viagem tem o valor de R$0,45 por kilometro,\n'
          'sendo assim sua viagem ficou no valor de {:.2f}'.format(vlg))