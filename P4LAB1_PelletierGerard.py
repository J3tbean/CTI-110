# Gerard Pelletier
# 3/20/2025
# P4LAB1
# Learning turtle graphics and loops.

import turtle 
win = turtle.Screen()
Brady = turtle.Turtle()

Brady.pensize(4)
Brady.pencolor("Blue")
Brady.shape("arrow")

side_num = 0
# Draw the Triangle
for triangle in (1,2,3):
    Brady.forward(100)
    Brady.left(120)

# Draw the Square
Brady.right(90)
while side_num <= 2:
    Brady.forward(100)
    Brady.left(90)
    side_num += 1
Brady.left(90)
Brady.forward(100)
Brady.right(90)
Brady.forward(35)

# Draw the door
for door in (1,2,3,4):
    Brady.forward(25)
    Brady.right(90)

win.mainloop()