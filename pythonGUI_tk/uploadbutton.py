from tkinter import *

window = Tk()
window.title("Text Box")
window.wm_minsize(height=200, width=400)
text1 = Text(height=5, width=20)
# Putting Cursor in the Text Box
text1.focus()
# Adds some text to begin with.
text1.insert(END, "Example")
# Gets current value in textbox at line 1, character 0
print(text1.get("1.0", END))
text1.pack()

window.mainloop()