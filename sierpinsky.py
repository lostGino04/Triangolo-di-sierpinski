import random
import turtle

#funzione disegnapunto che così non c'è bisogno di scrivere ogni volta lo schifo
def drawdot(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.dot(2)

#impostazioni di base
win = turtle.Screen()
win.setup(1000, 1000)
pen = turtle.Turtle()
pen.color("black")
pen.speed(10)
pen.hideturtle()

#vertici del triangolo
drawdot(300, -173.20507)
drawdot(-300, -173.20507)
drawdot(0, 346.41016)

#funzione main
def main():
    #si sceglie a caso da una lista di tuple il primo vertice da cui partire...
    pallino1 = random.choice([(300, -173.20507), (-300, -173.20507), (0, 346.41016)])
    #...e il secondo
    pallino2 = random.choice([(300, -173.20507), (-300, -173.20507), (0, 346.41016)])

    #si calcola il punto medio di entrambi
    x = (pallino1[0] + pallino2[0])/2
    y = (pallino1[1] + pallino2[1])/2
    
    #ciclo con ľalgoritmo principale
    for i in range(9999999):
        drawdot(x, y)
        nuovo_vertice = random.choice([(300, -173.20507), (-300, -173.20507), (0, 346.41016)])
        x = (x + nuovo_vertice[0])/2
        y = (y + nuovo_vertice[1])/2
main()

turtle.done()
