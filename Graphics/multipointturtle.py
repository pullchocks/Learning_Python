import turtle

# Create two turtle objects
avery = turtle.Turtle()
kate = turtle.Turtle()

# Move avery forward and turn right
avery.forward(50)
avery.right(90)
avery.forward(50)

# Move kate left and forward
kate.left(90)
kate.forward(100)

# Move avery forward and turn right again
avery.forward(50)
avery.right(90)
avery.forward(50)

# Move kate left and forward twice
kate.left(90)
kate.forward(100)
kate.left(90)
kate.forward(100)

# Move avery forward and turn right one last time
avery.forward(50)
avery.right(90)
avery.forward(50)

# Keep the turtle graphics window open
turtle.done()