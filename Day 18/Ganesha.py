import turtle as t

screen = t.Screen()
ganpati = t.Turtle()

blue = '#10557d'
white = '#ffffff'
red = '#ff0004'
black = '#000000'
yellow = '#ffb700'

screen.title('Ganpati Bappa')
ganpati.shape('turtle')

ganpati.color(blue,blue)
ganpati.begin_fill()
ganpati.left(angle = 130)
ganpati.forward(distance=55)
ganpati.right(90)
ganpati.forward(70)
ganpati.right(65)
ganpati.forward(70)
ganpati.right(80)
ganpati.forward(55)
ganpati.right(70)
ganpati.forward(66)
ganpati.end_fill()

ganpati.penup()
ganpati.forward(10)
ganpati.left(90)
ganpati.forward(12.5)
ganpati.pendown()

ganpati.color(yellow,yellow)
ganpati.begin_fill()
ganpati.forward(90)




