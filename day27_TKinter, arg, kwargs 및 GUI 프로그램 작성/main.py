from tkinter import *


def button_clicked():
    my_label["text"] = input.get()


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(row=0, column=0)
my_label.config(padx=50, pady=50)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(row=0, column=2)

# Entry
input = Entry(width=10)
input.grid(row=2, column=3)

# keep the window on screen
window.mainloop()

