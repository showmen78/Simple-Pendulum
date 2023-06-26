
''' 
--  SIMPLE PENDULUM BY @SHOWMEN DEY

--  THIS IS THE MAIN FILE 

--  CREATE WINDOW , CALLS THE PENDULUM CLASS 
'''

#IMPORTING LIBRARIES
import turtle
import time 
import math
from pendulum import Pendulum
from pendulum import FPS

WIDTH =800
HEIGHT= 600


# creating a window
wn = turtle.Screen()
#setting the width and height of the screen
wn.setup(width=WIDTH,height=HEIGHT)
#background color of the screen
wn.bgcolor("#046307")
#setting the animation on this window off
wn.tracer(0)

p= Pendulum(wn,turtle.Vec2D(0,200),rope_len=300,angle=math.radians(90))

while True:
    wn.update()
    p.update()
    time.sleep(1/FPS)


