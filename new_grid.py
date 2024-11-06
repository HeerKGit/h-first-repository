import turtle

def pixel(pixel_size):
    for x in range(4):
        turtle.forward(pixel_size)
        turtle.left(90)


def row(num_rows, pixel_size):
    r = 0
    while r < num_rows:
        
        pixel(pixel_size)
        turtle.forward(pixel_size)
        r+=1

def columns(num_columns, num_rows, pixel_size):

    c = 0

    while c < num_columns:
        row(num_rows, pixel_size)
        turtle.left(180)
        turtle.forward(pixel_size*num_rows)
        turtle.left(90)

        turtle.forward(pixel_size)
        turtle.left(90)

        c += 1



turtle.speed(0)
turtle.penup()
turtle.goto(-300,300)
turtle.pendown()
columns(20,20,30)