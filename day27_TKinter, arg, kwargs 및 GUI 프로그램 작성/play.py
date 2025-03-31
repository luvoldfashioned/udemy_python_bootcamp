from tkinter import *


def button_clicked():
    label = Label(text="엿먹어", font=("Arial", 24, "bold"))
    label.pack()


window = Tk()
window.title("엿먹어")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


button = Button(text="싫어 버튼", command=button_clicked)
button.pack()

window.mainloop()
