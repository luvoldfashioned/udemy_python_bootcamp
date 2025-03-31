# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(row=0, column=0)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

# Entry
input = Entry(width=10)
input.grid(row=2, column=2)