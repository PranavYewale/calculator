from calendar import SUNDAY
from textwrap import fill
from tkinter import *

root = Tk()
root.geometry("317x475")
root.title("Calculator")
root.iconbitmap("py.ico")
root.config(bg="#e6e6e6")
root.minsize(width=317, height=475)


# def calculate(event):
#     global scval
#     text = event.widget.cget("text")
#     print(text)
#     if text == "=":
#         pass
#     elif text == "C":
#         scval.set("")
#         screen.update()
#     else:
#         scval.set(scval.get() + text)
#         screen.update()


scval = StringVar()
scval.set("")

lb = Label(root, width=50, height=2, font="Lucida 20 bold")
lb.pack(fill=X)

lb1 = Label(root, text="0").place(x=100, y=1)

Button(root, text="≡  Standard                ", font="Lucida 18 bold",
       pady=1, padx=1, background="#e6e6e6", relief=GROOVE, border=0).place(x=0, y=0)

Button(root, text="↺", font="ArialRounded 18 bold",
       pady=1, padx=21, background="#e6e6e6", relief=GROOVE, border=0).place(x=244, y=0)

Button(root, text="%", font="ArialRounded 18 bold",
       pady=1, padx=21, background="light grey", relief=GROOVE, border=0).place(x=0, y=170)

Button(root, text="CE", font="ArialRounded 18 bold",
       pady=1, padx=13, background="light grey", relief=GROOVE, border=0).place(x=80, y=170)

Button(root, text="C", font="ArialRounded 18 bold",
       pady=1, padx=21, background="light grey", relief=GROOVE, border=0).place(x=160, y=170)


Button(root, text="⩤", font="ArialRounded 18",
       pady=3, padx=20, background="light grey", relief=GROOVE, border=0).place(x=240, y=170)


Button(root, text="1/x", font="ArialRounded 18",
       pady=3, padx=15, background="light grey", relief=GROOVE, border=0).place(x=1, y=221)

Button(root, text="x²", font="ArialRounded 18",
       pady=3, padx=21, background="#d6d6d6", relief=GROOVE, border=0).place(x=80, y=221)

Button(root, text="√x", font="ArialRounded 18",
       pady=3, padx=19, background="#d6d6d6", relief=GROOVE, border=0).place(x=160, y=221)

Button(root, text="÷", font="ArialRounded 18 bold",
       pady=1, padx=22, background="light grey", relief=GROOVE, border=0).place(x=240, y=221)


Button(root, text="9", font="Lucida 18 bold",
       pady=1, padx=23, background="White", relief=GROOVE, border=0).place(x=1, y=272)

Button(root, text="8", font="Lucida 18 bold",
       pady=1, padx=23, background="White", relief=GROOVE, border=0).place(x=80, y=272)

Button(root, text="7", font="Lucida 18 bold",
       pady=1, padx=23, background="White", relief=GROOVE, border=0).place(x=160, y=272)

Button(root, text="x", font="ArialRounded 18",
       pady=3, padx=24, background="light grey", relief=GROOVE, border=0).place(x=240, y=272)

Button(root, text="6", font="Lucida 18 bold",
       pady=1, padx=23, background="White", relief=GROOVE, border=0).place(x=1, y=323)

Button(root, text="5", font="Lucida 18 bold",
       pady=1, padx=23, background="White", relief=GROOVE, border=0).place(x=80, y=323)

Button(root, text="4", font="Lucida 18 bold",
       pady=1, padx=23, background="White", relief=GROOVE, border=0).place(x=160, y=323)

Button(root, text="–", font="ArialRounded 18",
       pady=3, padx=23, background="light grey", relief=GROOVE, border=0).place(x=240, y=323)


Button(root, text="3", font="Lucida 18 bold",
       pady=1, padx=23, background="White", relief=GROOVE, border=0).place(x=1, y=374)

Button(root, text="2", font="Lucida 18 bold",
       pady=1, padx=23, background="White", relief=GROOVE, border=0).place(x=80, y=374)

Button(root, text="1", font="Lucida 18 bold",
       pady=1, padx=23, background="White", relief=GROOVE, border=0).place(x=160, y=374)

Button(root, text="+", font="ArialRounded 18",
       pady=3, padx=22, background="light grey", relief=GROOVE, border=0).place(x=240, y=374)


Button(root, text="+/-", font="ArialRounded 18 bold",
       pady=1, padx=15, background="White", relief=GROOVE, border=0).place(x=1, y=425)

Button(root, text="0", font="Lucida 18 bold",
       pady=1, padx=23, background="White", relief=GROOVE, border=0).place(x=80, y=425)

Button(root, text=".", font="ArialRounded 18 bold",
       pady=1, padx=24, background="White", relief=GROOVE, border=0).place(x=160, y=425)

Button(root, text="=", font="Lucida 18",
       pady=3, padx=25, background="#4599db", relief=GROOVE, border=0).place(x=235, y=425)


root.mainloop()
