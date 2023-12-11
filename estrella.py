import turtle

def dibujar_estrella(size):
    for _ in range(9):
        turtle.forward(size)
        turtle.right(160)

turtle.pencolor("black")
turtle.pensize(3)
turtle.speed(3)

dibujar_estrella(300)

turtle.done()
