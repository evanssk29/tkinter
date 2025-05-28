from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)

tab1= Frame(notebook) # new frame for tab 1
tab2= Frame(notebook) # new frame for tab 2

notebook.add(tab1,text="Tab 1")
notebook.add(tab2,text="Tab 2")
notebook.pack(expand=True,fill="both")  # expand = expand to fill any space not otherwise used
                                        # fill = fill space on x and y axis

Label(tab1,text="Hello, this is tab 1",width=50,height=50).pack()
Label(tab2,text="Hello this is tab 2",width=50,height=50).pack()
window.mainloop()