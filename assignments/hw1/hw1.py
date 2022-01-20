"""
Name: <your name goes here – Logan Rager>
<hw1>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("The volume is", volume)


def shooting_percentage():
    shots = eval(input("How many shots were attempted? "))
    made = eval(input("How many shots were made? "))
    percentage = (made / shots) * 100
    print("Shooting percentage: ",percentage,"%")


def coffee():
    lbs = eval(input("How many pounds of coffee would you like? "))
    total = ((10.50 + 0.86) * lbs) + 1.50
    print("Your total is $", total)


def kilometers_to_miles():
    kilo = eval(input("Enter number of Kilometers: "))
    miles = kilo / 1.6
    print("That is", miles, "miles!")


if __name__ == '__main__':
    pass
