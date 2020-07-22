s = ''
while s != 'M' and s != 'F' and s != 'MASCULINO' and s !='FEMININO':
    s = str(input('Qual o sexo da pessoa [M/F] ? ')).strip().upper()#[0]
    if s != 'M' and s != 'F' and s != 'MASCULINO' and s !='FEMININO':
        print('A resposta está incorreta, digite somento com [M] para MASCULINO ou com [F] para FEMININO')
if s == 'M':
    s = 'Masculino'
if s == 'F':
    s = 'Feminino'
print('O sexo da pessoa é {}'.format(s))

#while s not in 'MmFf':
