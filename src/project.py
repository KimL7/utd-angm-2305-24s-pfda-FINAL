import turtle

display = turtle.Screen()
display.title("Cat Expression!") #Title of program
display.bgcolor("white")

# Update expressions later
display.register_shape("placeholder.gif") #image

cat = turtle.Turtle()
cat.shape("placeholder.gif") #image
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
    click += 1
    pen.clear()
    pen.write(f"Clicks: {click}", align="center", font=("Verdana", 40, "normal")) #text
cat.onclick(clicked)

display.mainloop()