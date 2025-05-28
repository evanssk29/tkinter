from tkinter import *

def doSomething(event):
    print("Mouse coordinates: " +str(event.x)+","+str(event.y))

window = Tk()

# window.bind("<Button-1>",doSomething) # left mouse click
# window.bind("<Button-2>",doSomething) # scroll wheel pressed
# window.bind("<Button-3>",doSomething) #  right click
# window.bind("<ButtonRelease>",doSomething)
# window.bind("<Enter>",doSomething) # entered the window
# window.bind("<Leave>",doSomething) # where left
window.bind("<Motion>",doSomething) # where the mouse moved

window.mainloop()