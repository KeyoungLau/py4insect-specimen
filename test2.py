from tkinter import *
import sys
root=Tk()
textbox=Text(root)
textbox.pack()
button1=Button(root, text='output', command=lambda : print('printing to GUI'))
button1.pack()

def redirector(inputStr):
    textbox.insert(INSERT, inputStr)

sys.stdout.write = redirector #whenever sys.stdout.write is called, redirector is called.

root.mainloop()
