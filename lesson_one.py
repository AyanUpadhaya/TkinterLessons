# Let's create a hello world application

from tkinter import *

#initialize app window
root = Tk()

root.title("New app")
root.geometry("400x400")

# we use label for displaying text
label1 = Label(root,text="Hello world")
label1.pack()
label1.config(font=('Arial',44))
label1.config(fg="black")
label1.config(bg="yellow")

# we use mainloop so that application doesn't get closed at starting
root.mainloop()
