import math

from graphics import *

def add_ten(nums):
    empty_list = []
    for num in nums:
        plus_10 = num + 10
        empty_list.append(plus_10)
    print(empty_list)


def square_each(nums):
    empty_list = []
    for num in nums:
        squared = num ** 2
        empty_list.append(squared)
    return empty_list


def sum_list(nums):
    sum_result = sum(nums)
    return sum_result


def to_numbers(nums):
    empty_list = []
    for num in nums:
        number_convert = float(num)
        empty_list.append(number_convert)
    return empty_list


def sum_of_squares(nums):
    empty_list = []
    for num in nums:
        split_string = num.split(",")
        new_string = to_numbers(split_string)
        new_list = square_each(new_string)
        answer = sum_list(new_list)
        empty_list.append(answer)
    print(empty_list)


def starter(weight, wins):
    if (150.0 <= weight <= 160.0) and wins >= 5:
        print("True")
        return True
    elif weight > 199.0 or wins > 20:
        print("True")
        return True
    else:
        print("False")
        return False


def leap_year(year):
    div = year % 4
    div2 = year % 100
    if div == 0 and div2 == 0:
        print("It is a leap year!")
        return True
    else:
        print("It is not a leap year :(")
        return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt((center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    win.getMouse()


def did_overlap(circle_one, circle_two):









if __name__ == '__main__':
    #add_ten([1, 2, 3, 4])
    #square_each([3, 5.7, 2])
    #sum_list([1, 2, 3.5, 4, 5, 6])
    #to_numbers(["3", "5.7", "2"])
    #sum_of_squares(["3, 7.2, 9", "6, 11, 10"])
    #starter(180.0, 30)
    #leap_year(400)
    did_overlap()
