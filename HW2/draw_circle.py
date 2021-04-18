# Draw Circle
"""
  Project: Draw Circle
  Author: Minsu Choe
  Date of last update: Mar. 12, 2021
"""

import turtle

# init
t=turtle.Turtle()
t.shape("turtle")

# define variable 
print("===Draw Circle Program===")
start_x = float(input("input x = "))
start_y = float(input("input y = "))
radius = int(input("input radius = "))

# move cursor location
t.home()
t.up()
t.goto(start_x,start_y-radius/2)
t.down()

# draw circle on canvas
t.circle(radius)

# end message
input("press any key to exit")