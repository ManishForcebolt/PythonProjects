from tkinter import *
window = Tk()
window.title("Convertor Mile to KM")
window.wm_minsize(height=400, width=500)
window.config(padx=2, pady=2)


# TODO: Adding Text

my_label = Label(text="Miles ", font=("Times", 20, "bold"))
my_label.grid(row=0, column=1)

my_label1 = Label(text="Kilometer= ", font=("Times", 20, "bold"))
my_label1.grid(row=1, column=1)

km_label = Label(text="0", font=("Times", 20, "bold"))
km_label.grid(row=1, column=2)
# TODO: Adding Entry box
input1 = Entry(width=20)
print(input1.get())
input1.grid(row=0, column=2)

# input1 = Entry(width=20)
# print(input1.get())
# input1.grid(row=1, column=2)


# TODO: Adding button to the window
def button1_clicked():
    miles = getint(input1.get())
    km = 1.607 * miles
    km_label.config(text=km)


button1 = Button(text="Convert", command=button1_clicked)
button1.grid(row=0, column=3)
window.mainloop()
