from turtle import *
import turtle as tk
tk.Screen()
tk.bgcolor("light yellow")
hideturtle()
speed(0)
pensize(5)
color("light yellow")

#making invisible triangle
goto(0,0)
right(60)
forward(100)
goto(0,0)
right(60)
forward(100)
left(120)
forward(100)

#making invisible square
for i in range(4):
    left(90)
    forward(100)

#making invisible pentagon
for i in range(5):
    left(72)
    forward(100)

##making invisible hexagon
for i in range(6):
    left(60)
    forward(100)

##making invisible
for i in range(7):
    left(51.428571428571)
    forward(100)

#same process reverse for visible to full colours
speed(3)
color("red")
begin_fill()
for i in range(7):
    backward(100)
    right(51.428571428571)
end_fill()
color("blue")
begin_fill()
for i in range(6):
    backward(100)
    right(60)
end_fill()
color("green")
begin_fill()
for i in range(5):
    backward(100)
    right(72)
end_fill()
color("yellow")
begin_fill()
for i in range(4):
    backward(100)
    right(90)
end_fill()
color("sky blue")
begin_fill()
for i in range(3):
    backward(100)
    right(120)
end_fill()


tk.mainloop()
