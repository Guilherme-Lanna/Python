from turtle import *


def click(x, y):
    print("Ponto:")
    print("x:" + str(x))
    print("y:" + str(y))
    goto(x, y)
    dot(5)
    text = "(" + str(x) + "," + str(y) + ")"
    write(text)


onscreenclick(click)

mainloop()