from tkinter import *

window = Tk()
window.title("Tkinter Example")
window.wm_minsize(width=500, height=400)

# TODO: Adding Label
my_label = Label(text="Output", font=("Times", 20, "bold"))
# my_label.pack(side="left")
my_label.grid(row=0, column=1)


# To embed new values to existing label we can do either of below two config new properties to label e.g.
# my_label["text"] = "New"
# my_label.config(text="New Text")

# TODO: Adding button to the window
# button1 to click and open select csv file
def button1_clicked():
    print("Button1 clicked")
    my_label["text"] = input1.get()


button1 = Button(text="Click", command=button1_clicked)
button1.grid(row=1, column=0)

# TODO: Adding Entry box
input1 = Entry(width=20)
print(input1.get())
input1.grid(row=0, column=0)

window.mainloop()
