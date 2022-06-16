import turtle

win = turtle.Screen()
win.title("Pong ")
win.bgcolor("pink")
win.setup(width=800, height=600)
win.tracer(0)


bazikon1 = turtle.Turtle()
bazikon1.speed(0)
bazikon1.shape("square")
bazikon1.shapesize(stretch_wid=6, stretch_len=1)
bazikon1.color("red")
bazikon1.penup()
bazikon1.goto(-350, 0)


bazikon2 = turtle.Turtle()
bazikon2.speed(0)
bazikon2.shape("square")
bazikon2.shapesize(stretch_wid=6, stretch_len=1)
bazikon2.color("white")
bazikon2.penup()
bazikon2.goto(350, 0)



topp = turtle.Turtle()
topp.speed(0)
topp.shape("circle")
topp.color("red")
topp.penup()
topp.goto(0, 0)
topp.dx = 0.3
topp.dy = 0.1


def bazikon1up():
    y = bazikon1.ycor()
    y +=25
    bazikon1.sety(y)
def bazikon1down():
    y = bazikon1.ycor()
    y -=25
    bazikon1.sety(y)

def bazikon2up():
    y = bazikon2.ycor()
    y +=25
    bazikon2.sety(y)
def bazikon2down():
    y = bazikon2.ycor()
    y -=25
    bazikon2.sety(y)


win.listen()
win.onkeypress(bazikon1up, "w")
win.onkeypress(bazikon1down, "s")

win.onkeypress(bazikon2up, "Up")
win.onkeypress(bazikon2down, "Down")


while True:
    win.update()
    topp.setx(topp.xcor() + topp.dx)  
    topp.sety(topp.ycor() + topp.dy)
    
    if topp.ycor() > 250:
        topp.sety(250)
        topp.dy *= -1
    if topp.ycor() < -250:
        topp.sety(-250)
        topp.dy *= -1
    if topp.xcor() < -350:
        topp.setx(-350)
        topp.dx *= -1
    if topp.xcor() > 350:
        topp.setx(350)
        topp.dx *= -1
   
    if (topp.xcor() < 290 and topp.xcor() > 330) and (topp.ycor() < bazikon1.ycor() + 50 and topp.ycor() > bazikon1.ycor() -50):
        topp.setx(290)
        topp.dx *= -1
    if (topp.xcor() < -290 and topp.xcor() > -330) and (topp.ycor() < bazikon2.ycor() + 50 and topp.ycor() > bazikon2.ycor() -50):
        topp.setx(290)
        topp.dx *= -1
