from tkinter import *


def button_clicked():
    mile = int(input.get())
    label_value.config(text=round(mile*1.6))


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

# Label
label_miles = Label(text="Miles", font=("Arial", 15, "normal"))
label_miles.grid(row=0, column=2)

label_is_equal_to = Label(text="is equal to", font=("Arial", 15, "normal"))
label_is_equal_to.grid(row=1, column=0)

label_km = Label(text="Km", font=("Arial", 15, "normal"))
label_km.grid(row=1, column=2)

label_value = Label(text=0, font=("Arial", 15, "normal"))
label_value.grid(row=1, column=1)

# Entry
input = Entry(width=10)
input.grid(row=0, column=1)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)

# keep the window on screen
window.mainloop()
