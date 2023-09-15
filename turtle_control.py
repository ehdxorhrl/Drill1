import turtle

def turtle_up():
    turtle.seth(90)
    turtle.forward(50)
    turtle.stamp()

def turtle_left():
    turtle.seth(180)
    turtle.forward(50)
    turtle.stamp()

def turtle_right():
    turtle.seth(0)
    turtle.forward(50)
    turtle.stamp()

def turtle_down():
    turtle.seth(270)
    turtle.forward(50)
    turtle.stamp()

def turtle_restart():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(turtle_up,'w')
turtle.onkey(turtle_left,'a')
turtle.onkey(turtle_right,'d')
turtle.onkey(turtle_down,'s')
turtle.onkey(turtle_up,'W')
turtle.onkey(turtle_left,'A')
turtle.onkey(turtle_right,'D')
turtle.onkey(turtle_down,'S')
turtle.onkey(turtle_restart,'Escape')
turtle.listen()
    
    
