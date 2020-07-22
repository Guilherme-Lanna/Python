#from turtle import *
#tracer(0)
#cores = ["red", "yellow", "green", "cyan", "blue", "magenta", "brown"]

#bgcolor("black")

#for i in range(len(cores)*40):
    #pencolor(cores[i % len(cores)])
    #fd(i)
    #rt((360 / len(cores))-1)

#update()
    #pencolor(cores[i])
   # fd(100)
    #rt(360 / len(cores))

from turtle import *

#tracer(0)

cores = ["red","yellow","green","cyan","blue","magenta"]
#cores = ["blue", "red", "yellow", "green"]

bgcolor("black")

for i in range(len(cores) * 100):
    pencolor(cores[i % len(cores)])
    fd(i)
    rt((360 / len(cores)) - 0.5)

#update()