# draw_square with Turtle graphic and loop
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("red")
t.width(3)
width = int(input("input width of square = "))
turn_angle = 90
loop_count = 0
t.home()
t.write(t.position())
start_x = - width//2
start_y = - width//2
t.up()
t.goto((start_x, start_y))
t.down()
while loop_count < 4:
    t.write(t.position())
    t.forward(width)
    t.left(turn_angle)
    loop_count = loop_count + 1
t.up(); t.home(); t.down()
input("press any key to exit")