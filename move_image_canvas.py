from tkinter import *

window = Tk()

def move_up(event):
    canvas.move(myimage,0,-10)
def move_left(event):
    canvas.move(myimage, -10, 0)
def move_down(event):
    canvas.move(myimage, 0, 10)
def move_right(event):
    canvas.move(myimage, 10, 0)

window.bind("<w>",move_up)
window.bind("<a>",move_left)
window.bind("<s>",move_down)
window.bind("<d>",move_right)
window.bind("<Up>",move_up)
window.bind("<Left>",move_left)
window.bind("<Down>",move_down)
window.bind("<Right>",move_right)


canvas = Canvas(window,width=500,height=500)
canvas.pack()

photo = PhotoImage(file='Burning 1.png')
myimage = canvas.create_image(0,0,image=photo,anchor=NW)

window.mainloop()