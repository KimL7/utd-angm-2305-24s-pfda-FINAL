import turtle
import pygame

expressions = ["placeholder.gif", "placeholder2.gif", "placeholder3.gif", "placeholder4.gif"]
count = 0

display = turtle.Screen()
display.title("Cat Expression!") #Title of program
display.bgcolor("white")

# Update expressions later
display.register_shape(expressions[count]) #image

cat = turtle.Turtle()
cat.shape(expressions[count]) #image
cat.speed(0)

click = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("black")
pen.penup()
pen.goto(0, 250)
pen.write(f"Clicks: {click}", align="center", font=("Verdana", 40, "normal")) #text

def clicked(x, y):
    global click
    global count
    click += 1
    count += 1
    if (count > 3):
        count = 0
    pen.clear()
    pen.write(f"Clicks: {click}", align="center", font=("Verdana", 40, "normal")) #text
cat.onclick(clicked)

display.mainloop()