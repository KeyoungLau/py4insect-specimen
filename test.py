import tkinter as tk 
from tkinter import messagebox 

class App(tk.Frame): 

    def __init__(self, master): 
     self.master = master 

     lbl1 = tk.Label(self.master, text = "Enter 2 numbers to be added \ntogether and click submit") 
     lbl1.grid(row = 0, column = 0, columnspan = 3) 

     self.entry1 = tk.Entry(self.master, width = 5) 
     self.entry1.grid(row = 1, column = 0) 

     self.lbl2 = tk.Label(self.master, text = "+") 
     self.lbl2.grid(row = 1, column = 1) 

     self.entry2 = tk.Entry(self.master, width = 5) 
     self.entry2.grid(row = 1, column = 2) 

     btn1 = tk.Button(self.master, text = "Submit", command = self.add_numbers) 
     btn1.grid(row = 2, column = 1) 

     self.lbl3 = tk.Label(self.master, text = "Sum = ") 
     self.lbl3.grid(row = 3, column = 1) 

     self.entry3 = tk.Entry(self.master, width = 10) 
     self.entry3.grid(row = 4, column = 1) 

     self.text1 = tk.Text(self.master, height = 1, width = 10) 
     self.text1.grid(row = 5, column = 1) 

    def add_numbers(self): 

     x = self.entry1.get() 
     y = self.entry2.get() 

     if x != "" and y != "": 
      sumxy = int(x) + int(y) 

      self.lbl3.config(text = "Sum = {}".format(sumxy)) 

      self.entry3.delete(0, "end") 
      self.entry3.insert(0, sumxy) 

      self.text1.delete(1.0, "end") 
      self.text1.insert(1.0, sumxy) 

      messagebox.showinfo("Sum of {} and {}".format(x,y), 
           "Sum of {} and {} = {}".format(x, y, sumxy)) 


if __name__ == "__main__": 

    root = tk.Tk() 
    myapp = App(root) 
    root.mainloop() 