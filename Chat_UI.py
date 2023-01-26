from threading import *
from tkinter import *
import os


window = Tk()
window.title("msg")
window.geometry("350x150+300+100")


txtYourMessage = Entry(window, width=50)
txtYourMessage.insert(0,"")
txtYourMessage.grid(row=1, column=0, padx=10, pady=10)

server = Entry(window, width=50)
server.insert(0,"")
server.grid(row=2, column=0, padx=10, pady=10)


def Message():
    os.system(f"msg * /server:{server.get()} {txtYourMessage.get()}")

btnSendMessage = Button(window, text="Send", width=20, command=Message)
btnSendMessage.grid(row=3, column=0, padx=10, pady=10)

window.mainloop()
