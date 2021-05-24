import turtle
screen = turtle.Screen
turtle = turtle.Turtle
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

number = 1
height = 1
width = 2

for i in numbers:
  turtle.write(numbers, True, align="center")
  turtle.write((0,0), True)
  
screen.exitonclick()


