from tkinter import *

window = Tk()

def doSomething(event):
    # print("You pressed: " + event.keysym)
    label.config(text=event.keysym)


window.bind('<Key>',doSomething)

label = Label(window,font=("Helvetica",100))
label.pack()

window.mainloop()