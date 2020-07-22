frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for i in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[i]
print('O inverso de \033[033m{}\033[m é \033[033m{}\033[m'.format(junto, inverso))
if inverso == junto:
    print('Essa frase é um palíndromo!')
else:
    print('Essa frase não é um palindromo!')