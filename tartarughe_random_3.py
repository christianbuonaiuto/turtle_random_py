import turtle
import random
win=turtle.Screen()   
win.screensize(600,400)
win.bgcolor("lightgreen")
win.setworldcoordinates(0,0,600,400)
n=int(input("Tartarughe da generare: "))
ring=turtle.Turtle()
ring.color("black")
ring.pensize(3)
ring.speed(10)
ring.goto(0,410)
ring.goto(610,410)
ring.goto(610,0)
ring.goto(0,0)
ring.ht()
tartaruga=[0]*n
for i in range(n):
    tartaruga[i]=turtle.Turtle()
    tartaruga[i].shape("turtle")
    tartaruga[i].penup()
    tartaruga[i].speed(2)
    tartaruga[i].goto(random.randint(0,600),random.randint(0,400))

while True:   
    for i in range(len(tartaruga)):
        x=random.randint(0,600)
        y=random.randint(0,400)
        A=tartaruga[i].towards(x,y) # angolatura
        B=tartaruga[i].heading()
        tartaruga[i].left(A-B) #sottraggo l'angolo attuale delle tartarughe
        tartaruga[i].speed(1)
        tartaruga[i].goto(x,y)
        if (x>=600 or y>=400):  #calcolo il rimbalzo delle tartarughe
            tartaruga[i].left(180)
            tartaruga[i].forward(random.randint(10,100))
        elif x<=0 or y<=0:
            tartaruga[i].left(180)
            tartaruga[i].forward(random.randint(10,100))
