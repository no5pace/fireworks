import turtle
import random

# set bg info
screen = turtle.Screen()
screen.bgcolor("black")
screen.colormode(255)
turtle.title("Fireworks")

# turtle info
t = turtle.Turtle()
t.speed(100)

# draw stars
for i in range(0,100,1):
  # only generate within the size of the frame
  x = random.randint(-300,300)
  y = random.randint(-200,200)
  t.penup()
  t.goto(x,y)
  t.pendown()
  
  # set the radius of the star
  size = random.randint(1,5)
  
  # set the color to white
  t.pencolor(255,255,255)
  
  # steps for drawing an individual star
  for i in range(0,5,1):
    t.forward(size)
    t.backward(size)
    t.left(72)

# draw fireworks forever
for i in range(0,20,1):
  # only generate within an area a little bit smaller than the frame
  x = random.randint(-250,250)
  y = random.randint(-150,150)
  t.penup()
  t.goto(x,y)
  t.pendown()
  
  # set the radius of the firework
  size = random.randint(1,100)
  
  # set the color
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  t.pencolor(r,g,b)
  
  # steps for drawing an individual firework
  for i in range(0,36,1):
    t.forward(size)
    t.backward(size)
    t.left(10)
