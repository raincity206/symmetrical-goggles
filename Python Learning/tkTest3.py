from tkinter import *


root = Tk()


def printWord(event):
	print("Me name is Blake!")

button1 = Button(root, text="Print my name!")
button1.bind("<Button-1>", printWord)
button1.pack()

# # # creating labels to display text
# theLabel = Label(root, text="This is too easy")

# # # .pack just packs it in there
# theLabel.pack()

# topFrame = Frame(root)
# topFrame.pack()
# bottomFrame = Frame(root)
# bottomFrame.pack()

# one = Label(root, text="One", bg="red", fg="white")
# one.pack()
 
# button1 = Button(topFrame, text="Button 1", bg="black", fg="red")
# button2 = Button(topFrame, text="Button 2", fg="blue")
# button3 = Button(topFrame, text="Button 3", fg="green")
# button4 = Button(topFrame, text="Button 4", fg="purple")

# button1.pack(fill=X)
# button2.pack()
# button3.pack()
# button4.pack()

# c = Checkbutton(root, text="Keep me logged in")
# c.grid(columnspan=2)

# .mainloop() continuesly shows your window on the diplay
root.mainloop()

