from tkinter import *

window = Tk()
window.title("Tkinter Example")
window.wm_minsize(width=500, height=400)
my_label = Label(text="Output", font=("Times", 100, "bold"))
# my_label.pack(side="left")
my_label.place(x=120, y=130)


# To embed new values to existing label we can do either of below two config new properties to label e.g.
# my_label["text"] = "New"
# my_label.config(text="New Text")

# TODO: Adding button to the window
# button1 to click and open select csv file
def button1_clicked():
    print("Button1 clicked")
    my_label["text"] = input1.get()


button1 = Button(text="Click", command=button1_clicked)
button1.place(x=2, y=1.5)

# TODO: Adding Entry box
input1 = Entry(width=20)
print(input1.get())
input1.place(x=100, y=2)

window.mainloop()
