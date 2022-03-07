from tkinter import Tk, Label, Button
from random import randint

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('400x300')
lbl = Label(window,
            text="Are you Stupid?",
            font=("Arial Bold", 25),
            justify="left")
lbl.pack()


def clicked():
    r1 = randint(2, 12) * 25
    r2 = randint(4, 6) * 25
    if not r1 == 200 or r2 == 100:
        btn.place(x=r1, y=r2)


def clicked2():
    clicked()
    btn.place_forget()
    btn2.pack_forget()
    lbl.configure(text="hehehe.. I knew it!")


btn2 = Button(window, text="Yes", bg="gray", fg="white", command=clicked2)
btn2.pack()

btn = Button(window, text="No", bg="gray", fg="white", command=clicked)
btn.pack()

window.mainloop()

