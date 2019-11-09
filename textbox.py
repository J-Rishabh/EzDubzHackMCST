import tkinter
from tkinter import *
root=Tk()
def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    print(inputValue)
    waiting = Label(root,text="Searching... This might take a while...")
    waiting.pack()

textBox=Text(root, height=2, width=100)
textBox.pack()
buttonCommit=Button(root, height=1, width=10, text="Search", 
                    command=lambda: retrieve_input())
buttonCommit.pack()

mainloop()
