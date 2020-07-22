# Exemplo de animação

from turtle import *
from math import *

# Inicialização

tracer(0)
rodando = True
angulo = 0
pos = 0
fps = 60


def desenha():
    global angulo, fps, pos, rodadndo

    if not rodando:
        ontimer(desenha, int(1000 / fps))
        return

    # Limpa
    reset()

    # Desenha
    pu()
    goto(sin(pos) * 100, 0)
    pd()
    rt(angulo)
    for i in range(5):
        fd(100)
        rt(360 / 5)

    # Atualiza
    ht()
    update()
    angulo = angulo + 60 / fps
    pos = pos + 5 / fps

    # Repetir
    ontimer(desenha, int(1000 / fps))


def clica(x, y):
    global rodando
    rodando = not rodando


onscreenclick(clica)
desenha()
mainloop()