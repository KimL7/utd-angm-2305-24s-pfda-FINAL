import turtle
import pygame

expressions = ["placeholder.gif", "placeholder2.gif", "placeholder3.gif", "placeholder4.gif"]
count = 0

display = turtle.Screen()
display.title("Cat Expression!") # Title of program
display.bgpic("background.gif")

for shape in expressions:
    display.register_shape(shape)

cat = turtle.Turtle()
cat.shape(expressions[0]) # Image
cat.speed(0)

click = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("black")
pen.penup()
pen.goto(0, 250)
pen.write(f"Clicks: {click}", align="center", font=("Verdana", 40, "normal")) # Text

pygame.mixer.init()

audio_file = "meow.mp3" # Sound
click_sound = pygame.mixer.Sound(audio_file)

display.addshape("paw.gif") # Paw Image

def clicked(x, y):
    global click
    global count

    click += 1
    count += 1

    # Click sound effect
    click_sound.play()
    
    if count % 10 == 0:
        next_index = (expressions.index(cat.shape()) + 1) % len(expressions)
        cat.shape(expressions[next_index])
    
    paw = turtle.Turtle()
    paw.shape("paw.gif")
    paw.penup()
    paw.goto(x, y)
    paw.stamp() 

    pen.clear()
    pen.write(f"Clicks: {click}", align="center", font=("Verdana", 40, "normal")) # Text

cat.onclick(clicked)

display.mainloop()
