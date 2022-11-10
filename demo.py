from tkinter import *

root = Tk()

# 1 EXAMPLE

# label1 = Label(root, text="hello world")
# label1.pack()

# 2 EXAMPLE

# newframe = Frame(root)
# newframe.pack()

# otherframe = Frame(root)
# otherframe.pack(side=BOTTOM)

# button1 = Button(newframe, text="click here", fg="Red")
# button2 = Button(otherframe, text="click here", fg="Blue")


# button1.pack()
# button2.pack()


# 3. EXAMPLE

# label3 = Label(root, text='First Name ',bg="Red",fg="white")
# label4 = Label(root, text='Last Name ')

# entry1 = Entry(root)
# entry2 = Entry(root)

# label3.grid(row=0,column=0)
# label4.grid(row=1,column=0)

# entry1.grid(row=0,column=1)
# entry2.grid(row=1,column=1)

# 4. EXAMPLE

# label5 = Label(root, text='First ', bg="Red", fg="white")
# label5.pack(fill=X)

# label6 = Label(root, text='Second ', bg="Blue", fg="Green")
# label6.pack(fill=Y, side=LEFT)

# 5. EXAMPLE

# def dosomething():
#     print("you clicked the button")


# button1 = Button(root, text="click here", command=dosomething)
# button1.pack()

# 6. EXAMPLE

# class MyButtons:
#     def __init__(self,rootone):
#         frame=Frame(rootone)
#         frame.pack()

#         self.printbutton=Button(frame,text="click here",command=self.printmessage)
#         self.printbutton.pack()

#         self.quitbutton=Button(frame,text="Exit",command=frame.quit)
#         self.quitbutton.pack(side=LEFT)

#     def printmessage(self):
#         print("button clicked")

# b=MyButtons(root)

# 7. EXAMPLE

def function1():
    print("menu item clicked")


mymenu = Menu(root)
root.config(menu=mymenu)

submenu = Menu(mymenu)
mymenu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="project", command=function1)
submenu.add_command(label="save", command=function1)

submenu.add_separator()
submenu.add_command(label="Exit", command=function1)

Newmenu = Menu(mymenu)
mymenu.add_cascade(label="edit", menu=Newmenu)
Newmenu.add_command(label="undo", command=function1)

toolbar = Frame(root, bg="Pink")
insertbutton = Button(toolbar, text="Insert File", command=function1)
insertbutton.pack(side=LEFT, padx=2, pady=3)

printbutton = Button(toolbar, text="print", command=function1)
printbutton.pack(side=LEFT, padx=2, pady=3)

toolbar.pack(side=TOP, fill=X)


root.mainloop()
