import turtle,math
t = turtle.Turtle()
turtle.bgcolor("black")
t.setpos(0,-200)
t.color("red")
t.hideturtle()
t.speed(10)

t.left(60)
t.forward(294)

for i in range(150):
    t.forward(2)
    t.right(math.tan(40))
    
t.right(90)
    
for i in range(150):
     t.forward(2)
     t.right(math.tan(40))
    
t.forward(297)
turtle.done()    