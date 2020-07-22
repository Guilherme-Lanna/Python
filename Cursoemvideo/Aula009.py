frase = ('   Curso em Vídeo Python   ')
print(len(frase.strip()))

frase1 = ('\nCurso em Vídeo Python\n')
print(frase1.replace('Python', 'Android'))

frase2 = ('\nCurso em Vídeo Python\n')
frase2 = frase2.replace('Python', 'Android')
print(frase2)

frase3 = ('\nCurso em Vídeo Python\n')
print(frase3[1:15:2])

frase4 = ('\nCurso em Vídeo Python\n')
print(frase4.upper().count('O'))

frase5 = ('\nCurso em Vídeo Python\n')
print('Curso' in frase5)

frase6 = ('\nCurso em Vídeo Python\n')
print(frase6.find('Vídeo'))

frase7 = ('\nCurso em Vídeo Python\n')
print(frase7.lower().find('vídeo'))

frase8 = ('\nCurso em Vídeo Python\n')
print(frase8.split())

frase9 = ('\nCurso em Vídeo Python\n')
dividido = frase9.split()
print(dividido[0])

frase10 = ('\nCurso em Vídeo Python\n')
dividido = frase10.split()
print(dividido[2] [3])
