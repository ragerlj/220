def number_words():
    file = open('number words.py', 'r')
    for line in file:
        for word in line.split():
            print(word)


def hourly_wages():
    file = open('hourly_wages.txt')


def calc_check_sum(isbn):
    isbn2 = isbn[ : :-1]
    sum = 0
    for i in range(len(isbn)):
        num = int(isbn2[i]) * (i + 1)
        sum = sum + num
    print("Sum is:", sum)
calc_check_sum("0072946520")


def send_message(file_name,friend_name):
    friend_name+=".txt"
    ftr = open(file_name, "r")
    lines = ftr.readlines()
    ftr.close()
    ftr = open(friend_name, "w")
    for str in lines:
        ftr.write(str)
    ftr.close()
    print("\nFile Copied Successfully!")
send_message("myFile.txt","Bob")