num = int(input('Quantos números deseja apresentar da sequência Fibonacci: '))
cont = 1
anterior = 0
proxima = 1
soma = 1
while cont <= num:
     print(anterior, end=' -> ')
     cont += 1
     soma = proxima + anterior
     anterior = proxima
     proxima = soma
print('Fim')