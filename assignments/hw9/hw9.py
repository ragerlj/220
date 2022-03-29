from random import *
def get_words(file_name):
    words = []
    file = open(file_name, 'r')
    file.readline()
    for line in file:
        words.append(line.strip())
    return words


def get_random_word():
     get_words('words.txt') 















def letter_in_secret_word(letter, secret_word):
    pass




#def already_guessed(letter, guesses):



#def make_hidden_secret(secret_word, guesses):



#def won(guessed):



#def play_graphics(secret_word):



#def play_command_line(secret_word):



if __name__ == '__main__':
    get_random_word()
    # play_command_line(secret_word)
    # play_graphics(secret_word)