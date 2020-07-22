from turtle import *
from random import randrange


def galho(tam, larg, p):
    ang = randrange(20, 50)
    tam = tam * (randrange(70, 120) / 100)

    if p < 1:
        return
    width(larg)
    lt(ang / 2)
    fd(tam)
    galho(tam * 0.7, larg * 0.8, p - 1)
    width(larg)
    bk(tam)
    rt(ang)
    fd(tam)
    galho(tam * 0.7, larg * 0.8, p - 1)
    bk(tam)
    lt(ang / 2)


# tracer(0)

lt(90)
for i in range(20):
    pu()
    goto(i * randrange(20, 50) - 400, -200)
    pd()

    width(6)
    fd(randrange(10, 100))
    galho(50, 5, 9)

# update()