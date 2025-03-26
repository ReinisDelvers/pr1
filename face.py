from turtle import *

speed(100000)
ht()


fillcolor("yellow")
begin_fill()
for i in range(360):
    forward(1)
    left(1) 
end_fill()
penup()
left(90)
forward(30)
left(90)
for i in range(32):
    forward(1)
    right(2)
left(180)
pendown()
for i in range(64):
    forward(1)
    left(2)
penup()
left(180)
for i in range(32):
    forward(1)
    right(2)
right(90)
forward(40)
right(110)

pendown()
for i in range(15):
    forward(1)
    left(3)
penup()
left(180)
for i in range(15):
    forward(1)
    right(3)
right(160)
forward(15)
left(90)
forward(15)
pendown()
fillcolor("white")
begin_fill()
for i in range(360):
    forward(1/8)
    right(1) 
end_fill()
penup()
right(90)
forward(4)
right(90)
forward(2)
left(180)
pendown()
fillcolor("black")
begin_fill()
for i in range(360):
    forward(1/20)
    right(1) 
end_fill()
penup()
forward(2)
left(90)
forward(34)
right(90)
pendown()
fillcolor("white")
begin_fill()
for i in range(360):
    forward(1/8)
    left(1) 
end_fill()
penup()
left(90)
forward(4)
left(90)
forward(2)
right(180)
pendown()
fillcolor("black")
begin_fill()
for i in range(360):
    forward(1/20)
    left(1) 
end_fill()
penup()





Screen().exitonclick()


# print(f"Current angle: {heading()}")