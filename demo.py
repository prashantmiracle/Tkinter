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

label3 = Label(root, text='First Name ')
label4 = Label(root, text='Last Name ')

entry1 = Entry(root)
entry2 = Entry(root)

label3.grid(row=0,column=0)
label4.grid(row=1,column=0)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)


root.mainloop()
