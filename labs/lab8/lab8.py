from graphics import *
from random import randint
from random import *
def get_random(move_amount):
    random = randint(1, move_amount)
    neg_rand = randint(1, -move_amount)
    list = range(neg_rand, random)
    print(list)

def did_collide(circle_ball, circle_ball2):
    if circle_ball - circle_ball2 == 0:
        return True
    else:
        return False


#def hit_verticle(circle_ball, Graphwin):





def main():
    win = GraphWin('Collision', 800, 600)
    radius = 10
    random_point1 = Point(randint(10, 790), randint(10,790))
    random_point2 = Point(randint(10, 790), randint(10, 790))
    ball1 = Circle(Point(400, 300), radius)
    ball2 = Circle(Point(100,200), radius)
    #ball2.draw(win)
    ball1.draw(win)

    dx = 1
    dy = 1
    dx2 = 1


    y_floor = radius
    y_celing = win.getHeight()- radius
    x_floor = radius
    x_celing = win.getWidth() - radius

    color_list = ['red', 'blue', 'green', 'purple', 'yellow', 'black', 'white']
    color_random = randint(0,6)


    while True:
        ball1.move(dx, dy)
        ball2.move(dx,dy)
        if (ball1.getCenter().getY() <= y_floor or ball1.getCenter(). getY() >= y_celing) or (ball2.getCenter().getY() <= y_floor or ball2.getCenter().getY() >= y_celing):
            dy = -dy
            ball1.setFill(color_list[color_random])
        elif (ball1.getCenter().getX() <= x_floor or ball1.getCenter().getX() >= x_celing) or (ball2.getCenter().getX() <= x_floor or ball2.getCenter().getX() >= x_celing):
            dx = -dx
            ball1.setFill(color_list[color_random])





if __name__ == '__main__':
    main()