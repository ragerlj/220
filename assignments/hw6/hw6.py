def cash_converter():
    integer = eval(input("Enter an integer: "))
    new = "That is ${}.00".format(integer)
    print(new)


def encode():
    message = input("What message would you like to Encrypt? ")
    key = eval(input("Enter Key number: "))
    nums = " "
    for letter in message:
        num = ord(letter) + key
        nums = nums + str(num) + " "
        print(chr(num), end=" ")


def sphere_area():
    pi = 22/7
    radian = float(input("Radius of sphere: "))
    area = 4 * pi * radian **2
    volume = (4/3) * (pi * radian **3)
    print("Surface area is ", area)
    print("Volume is ", volume)



def sum_n():
    n = eval(input("How many natural numbers do you want the sum of?"))
    total = 0
    for i in range(n):
        total += i + 1
    return total

def sum_n_cubes():
    n = eval(input("How many natural numbers do you want the sum of? "))
    total = 0
    for i in range(n):
        total += (i + 1) **3
    return total


def encode_better():
    message = input("What word would you like to be encrypted")
    key_word = input("What is the key word?")
    nums = " "
    ace_val = int(len(message)/3)
    for i in range(ace_val):
        for letter in key_word:
            ord_val = ord(letter) + 1
            print(ord_val, end=" ")
    message_val = ord(message) + (ord_val+ 1)
    print(message_val)




