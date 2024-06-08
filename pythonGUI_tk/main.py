# import tkinter
from tkinter import *

window = Tk()
window.title("Tkinter Example")
window.wm_minsize(width=500, height=600)

my_label = Label(text="Click this button", font=("Times", 24, "bold"))
# my_label.pack(side="left")
my_label.pack()


# To embed new values to existing label we can do either of below two config new properties to label e.g.
# my_label["text"] = "New"
# my_label.config(text="New Text")

# TODO: Adding button to the window
# button1 to click and open select csv file
def button1_clicked():
    print("Button1 clicked")
    my_label["text"] = input1.get()


button1 = Button(text="Open", command=button1_clicked)
button1.pack()

# TODO: Adding Entry box
input1 = Entry(width=20)
print(input1.get())
input1.pack()

# TODO: Adding Text box
text1 = Text(height=5, width=20)
# Putting Cursor in the Text Box
text1.focus()
# Adds some text to begin with.
text1.insert(END, "Example")
# Gets current value in textbox at line 1, character 0
print(text1.get("1.0", END))
text1.pack()


# TODO: Adding a spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# TODO: Adding Scale from 1 to 100
# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# TODO: Adding the Checkbutton

def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    if checked_state.get() == 0:
        print("Unchecked", checked_state.get())
    else:
        print("Checked", checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Check Button?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# TODO: Radio Button
def radio_used():
    print(radio_state.get())
# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton3 = Radiobutton(text="Option3", value=3, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()


# TODO: Adding List to the GUI
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=3)
trainees = ["Ravi", "Manas", "Ritvik", "Sundar", "Kartik", "Navjeet"]
for item in trainees:
    listbox.insert(trainees.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
