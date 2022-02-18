def name_reverse():
    name = input("Enter name (first last): ")
    first_name = name.split()[0]
    last_name = name.split()[1]
    print(last_name, first_name)


def company_name():
    link = input("What is the Company's domain? ")
    length = len(link)
    name = link[4:length-4]
    print(name)


def initials():
    x = eval(input("How many students? "))
    y = 0
    for i in range(x):
        name =  input("What is name of student {}? ".format(i+1))
        first_name = name.split()[0]
        last_name = name.split()[1]
        name_list = [first_name, last_name]
        print(first_name[0], last_name[0])


def names():
    names = input("Enter list of names: ")
    names_list = names.split(', ')
    for i in names_list:
        initials = i.split(" ")
        print(initials[0][0]+initials[1][0])


def thirds():
    x = eval(input("How many Sentences? "))
    for i in range(x):
        sentence = input("What is sentence {}?".format(i+1))
        z = sentence[ : :3]
        print(z)


def word_average():
    x = input("Enter a Sentence: ")
    average = len(x.replace(' ',"")) / len(x.split())
    print(average)


def pig_latin():
    sentence = input("What is sentence: ")
    for i in range()