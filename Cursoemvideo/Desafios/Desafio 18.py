import math
ang = float(input('Digite o angulo : '))
seno = math.sin(math.radians(ang))
cose = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O seno do seu angulo é = {:.2f}'.format(seno))
print('O coseno do seu angulo é = {:.2f}'.format(cose))
print('A tangente do seu angulo é = {:.2f}'.format(tang))