  # Python Turtle was the program used to draw
# Rainbow Benzene
# Using Turtle Programming
# Link to website I found it on is https://www.geeksforgeeks.org/turtle-programming-python/

import turtle
colors = ['red', 'blue']
t = turtle.Pen()
turtle.bgcolor('white')
for x in range(360):
	t.pencolor(colors[x%2])
	t.width(x//100 + 1)
	t.forward(x)
	t.left(59)

