from graphics import *

win = GraphWin("Door", 700, 700)
point1 = Point(250,200)
point2 = Point(450, 700)
rect = Rectangle(point1, point2)

point3 = Point(250, 50)
point4 = Point(450, 150)
closing_rect = Rectangle(point3, point4)


rect.draw(win)
closing_rect.draw(win)
rect.setFill('Red')

exit_text_point = Point(350, 100)
exit_text = Text(exit_text_point, 'Exit')
exit_text.draw(win)

door_text_point = Point(350, 450)
open = 'open'
door_text = Text(door_text_point, open)
door_text.draw(win)



while True:
    if (250 == win.getMouse() == 450) and (200 == win.getMouse() == 700):
        rect.setFill('Blue')
        open = 'closed'





    input('')
