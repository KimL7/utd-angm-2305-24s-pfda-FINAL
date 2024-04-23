import turtle

wn = turtle.Screen()
wn.title("Cat Expression!")
wn.bgcolor("white")

wn.register_shape("placeholder.gif")

cat = turtle.Turtle()
cat.shape("placeholder.gif")
cat.speed(0)

wn.mainloop()