from datetime import date
print('-=-'*40)
print('Vamos ver em qual categoria o atleta se encaixa.')
print('-=-'*40)
atual = date.today().year
nascimento = int(input('Qual o ano de nascimento do atleta? '))
idade = atual - nascimento
if idade <= 9:
    print('O atleta se encaixa na categoria \033[1;35mmirim\033[m!')
elif idade > 9 and idade <= 14:
    print('O atleta se encaixa na categoria \033[1;35minfantil\033[m!')
elif idade > 14 and idade <= 19:
    print('O atleta se encaixa na categoria \033[1;35mjunior\033[m!')
elif idade > 19 and idade <= 20:
    print('O atleta se encaixa na categoria \033[1;35msênior\033[m!')
elif idade > 20:
    print('O atleta se encaixa na categoria \033[1;35mmaster\033[m!')