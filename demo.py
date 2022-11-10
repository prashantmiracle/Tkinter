from tkinter import *

root = Tk()

# label1 = Label(root, text="hello world")
# label1.pack()

newframe = Frame(root)
newframe.pack()

otherframe = Frame(root)
otherframe.pack(side=BOTTOM)

button1 = Button(newframe, text="click here", fg="Red")
button2 = Button(otherframe, text="click here", fg="Blue")


button1.pack()
button2.pack()

root.mainloop()
