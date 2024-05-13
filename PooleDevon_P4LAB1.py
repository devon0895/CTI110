#Devon Poole
#3/26/2024
#P4LAB1
#Using loops and turtles to draw shapes


import turtle
win = turtle.Screen()
timmy = turtle.Turtle()

#add some display options
timmy.pensize(4)
timmy.pencolor("purple")
timmy.shape('arrow')


for side in range(4):
    timmy.forward(75)
    timmy.left(90)


#While loop to draw the triangle
counter = 0
while counter < 3:
    timmy.forward(75)
    timmy.left(120)
    counter += 1
