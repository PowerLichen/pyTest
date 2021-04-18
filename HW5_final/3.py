"""
  Project: draw polygon
  Author: Minsu Choe
  StudentID: 21511796
  Date of last update: Apr. 5, 2021
"""
import turtle
import math

# draw polygon function
def drawPolygon(x,y,n,width):
    # check polygon vertex number
    if n<3:
        return

    # define turtle
    t= turtle.Turtle()
    # initialize turtle
    t.color("blue")
    t.width(4)

    # move to main coordinates
    t.up()
    t.goto((x,y))
    t.down()

    # draw dot and write (x,y) in main coordinates 
    t.dot(10,"red")
    t.write(t.position())
    

    loop_count=0

    # set start coordinates
    if n%2==0:
        # set start coordinates if even number
        start_x = x - width/2
        start_y = y + (width/2)/math.tan(math.radians(180/n))
        t.up()
        t.goto((start_x,start_y))
        t.down()
    else:
        # set start coordinates if odd number
        start_x = x
        start_y = y + width/2/math.sin(math.radians(180/n))
        t.up()
        t.goto((start_x,start_y))
        t.down()
        t.right(180/n)
    
    # draw line
    while loop_count<n:
        t.dot(10,"red")
        t.write(t.position())
        t.forward(width)
        t.right(360/n)
        loop_count+=1


#input arguments
x, y, num, width = map(int, input("input center_x, center_y, num_vertex and side_length : ").split())

drawPolygon(x,y,num,width)

input("press any key to exit")