

from graphics import *

def Vigenere_Cipher():
    #objects
    win = GraphWin("Vigenere", 400, 500)
    encode_txt = Text(Point(200 , 350), "Encode")
    encode_txt.draw(win)

    message_txt = Text(Point(200, 70), "Message to encode")
    message_entry = Entry(Point(200, 100), 30)
    message_entry.draw(win)
    message_txt.draw(win)

    key_txt = Text(Point(200, 170), "Enter keyword")
    key_entry = Entry(Point(200, 200), 20)
    key_entry.draw(win)
    key_txt.draw(win)


    message = message_entry.getText()
    key = key_entry.getText()



    win.getMouse()
    win.close()

    return (message, key)

Vigenere_Cipher()

