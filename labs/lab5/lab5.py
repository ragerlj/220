from graphics import Point, GraphWin
def triangle():
    win = GraphWin("Triangle", 700, 700)
    print(win)



def process_string():
    x = input("Enter a string: ")
    length = len(x)
    first_letter = x[0]
    last_letter = x[length-1]
    print(first_letter)
    print(last_letter)
    print(x[2], x[5])
    print(first_letter + last_letter)
    for i in range(10):
        print(x[1:5])

    y = -1
    for i in range(length):
        y = y + 1
        print(x[y])
    print(length)


def process_list():
    pt = Point(5,10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)

    x = values[0] + values[2]
    print(x)

    x = values[1] + values[1] + values[1] + values[1] + values[1]
    print(x)

    x = [values[2], values[3], values[4]]
    print(x)

    x = [values[2], values[3], values[0]]
    print(x)

    x = [values[2], values[0], float(values[5])]
    print(x)

    x = values[0] + values[2] + float(values[5])
    print(x)

    x = len(values)
    print(x)


def another_series():
    y = eval(input("How many terms? "))
    term = 0
    for i in range(y):
        term += 1
        print((term % 6) + 2)




def target():
    from graphics import GraphWin, Point, Circle
    width = 700
    height = 700
    win = GraphWin("Target", width, height)

    point_center = Point(width/2,height/2)
    big_circle = Circle(point_center, height / 4)

    medium_circle = Circle(point_center, height / 3)

    small_circle = Circle(point_center, height / 2)

    extra_small_circle = Circle(point_center, height/ 1)

    big_circle.draw(win)
    medium_circle.draw(win)
    small_circle.draw(win)
    extra_small_circle.draw(win)

    extra_small_circle.setFill("red")


    input("Hit enter to exit ")