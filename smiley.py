import turtle

def draw_circle(x,y,color,radius):

    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.circle(radius)
    turtle.end_fill()


def main():
    draw_circle(0,100,'yellow', 50)
    draw_circle(-100,200,'pink', 50)
    input()

if __name__ == '__main__':
    main()