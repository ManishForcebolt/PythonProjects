from tkinter import *

window = Tk()
window.title("CountDown")
window.config(bg="#f7f5dd", padx=60, pady=60)

title_label = Label(text="Timer", fg="green", bg="#f7f5dd", font=("Times", 80, "bold"))
title_label.grid(row=0, column=0)
canvas = Canvas(width=400, height=400, bg="#f7f5dd", highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(200, 200, image=tomato_img)
canvas.create_text(200, 200, text="00:00", fill="white", font=("Times", 55, "bold"))
canvas.grid(row=1, column=0)
start_button = Button(text="Start", highlightthickness=0)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(row=2, column=1)

window.mainloop()
