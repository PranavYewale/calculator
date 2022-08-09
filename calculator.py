from tkinter import *
import tkinter.messagebox as msg
from time import strftime

root = Tk()
root.geometry("317x475+600+200")
root.title("Calculator")
root.iconbitmap("py.ico")
root.config(bg="#e6e6e6")
root.minsize(width=317, height=475)


def change():
    root.geometry(f"317x475+-10+-80")


def rechange():
    root.geometry("317x475+600+200")


eq = ""


def show(value):
    global eq
    eq += value
    lb1.config(text=eq)
    lb2.config(text=eq)


def clear():
    global eq
    eq = ""
    lb1.config(text=eq)
    lb2.config(text=eq)


def calculate():
    global eq
    global resul
    resul = ""
    if eq != "":
        try:
            resul = eval(eq)
        except:
            resul = "Error"
            eq = ""
    lb2.config(text=resul)


def none():
    msg.showinfo("Coming Soon..", "This Feature Does'nt Exists")


def save():
    F = open("History.txt", "a")
    F.write(f" {time}{eq,resul}\n")
    F.close()
    msg.showinfo("Done", "Saved")


def time():
    t = StringVar()
    t = strftime("%H:%M:%S %p")


f = Frame(root)
f.place(x=15, y=50)

f2 = Frame(root)
f2.place(x=10, y=80)

lb1 = Label(f, text="", background="#e6e6e6",
            font="Lucida 20 bold", border=0, fg="grey")

lb1.pack(anchor=E)

lb2 = Label(f2, text="", background="#e6e6e6",
            font="Lucida 40 bold", border=0)
lb2.pack(anchor=E)


b = Button(root, text="≡", font="BahnschriftSemiLightSemiConde 18 bold",
           pady=1, padx=1, background="#e6e6e6", relief=GROOVE, border=0, command=none).place(x=0, y=0)

l = Label(root, text="Standard ", font="BahnschriftSemiLightSemiConde 18 bold",
          pady=1, padx=1, background="#e6e6e6", relief=GROOVE, border=0).place(x=35, y=7)


l = Button(root, text="⇱", font="Lucida 18 ",
           pady=1, padx=1, background="#e6e6e6", relief=GROOVE, border=0, command=change).place(x=160, y=0)


Button(root, text="↺", font="ArialRounded 18 ",
       pady=3, padx=21, background="#e6e6e6", relief=GROOVE, border=0, command=save).place(x=244, y=0)


Button(root, text="%", font="ArialRounded 18 bold",
       pady=1, padx=21, background="light grey", relief=GROOVE, border=0, command=lambda: show("%")).place(x=0, y=170)

Button(root, text="CE", font="ErasLightITC 15 ",
       pady=7, padx=19, background="light grey", relief=GROOVE, border=0, command=lambda: clear()).place(x=80, y=170)

Button(root, text="C", font="ErasLightITC 18 bold",
       pady=1, padx=21, background="light grey", relief=GROOVE, border=0, command=lambda: clear()).place(x=160, y=170)


Button(root, text="↻", font="ArialRounded 18 bold",
       pady=2, padx=22, background="light grey", relief=GROOVE, border=0, command=rechange).place(x=240, y=170)


Button(root, text="1/x", font="ErasLightITC  16",
       pady=6, padx=18, background="light grey", relief=GROOVE, border=0, command=lambda: show("*1/")).place(x=1, y=221)

Button(root, text="x²", font="ArialRounded 18",
       pady=3, padx=21, background="#d6d6d6", relief=GROOVE, border=0, command=lambda: show("**")).place(x=80, y=221)

Button(root, text="√x", font="ArialRounded 18",
       pady=3, padx=19, background="#d6d6d6", relief=GROOVE, border=0, command=lambda: show("√")).place(x=160, y=221)

Button(root, text="÷", font="ArialRounded 18 bold",
       pady=1, padx=22, background="light grey", relief=GROOVE, border=0, command=lambda: show("/")).place(x=240, y=221)


Button(root, text="9", font="Lucida 18 bold",
       pady=1, padx=23, background="White", relief=GROOVE, border=0, command=lambda: show("9")).place(x=1, y=272)

Button(root, text="8", font="Lucida 18 bold",
       pady=1, padx=23, background="White", relief=GROOVE, border=0, command=lambda: show("8")).place(x=80, y=272)

Button(root, text="7", font="Lucida 18 bold",
       pady=1, padx=23, background="White", relief=GROOVE, border=0, command=lambda: show("7")).place(x=160, y=272)

Button(root, text="x", font="ArialRounded 18",
       pady=3, padx=24, background="light grey", relief=GROOVE, border=0, command=lambda: show("*")).place(x=240, y=272)

Button(root, text="6", font="Lucida 18 bold",
       pady=1, padx=23, background="White", relief=GROOVE, border=0, command=lambda: show("6")).place(x=1, y=323)

Button(root, text="5", font="Lucida 18 bold",
       pady=1, padx=23, background="White", relief=GROOVE, border=0, command=lambda: show("5")).place(x=80, y=323)

Button(root, text="4", font="Lucida 18 bold",
       pady=1, padx=23, background="White", relief=GROOVE, border=0, command=lambda: show("4")).place(x=160, y=323)

Button(root, text="–", font="ArialRounded 18",
       pady=3, padx=23, background="light grey", relief=GROOVE, border=0, command=lambda: show("-")).place(x=240, y=323)


Button(root, text="3", font="Lucida 18 bold",
       pady=1, padx=23, background="White", relief=GROOVE, border=0, command=lambda: show("3")).place(x=1, y=374)

Button(root, text="2", font="Lucida 18 bold",
       pady=1, padx=23, background="White", relief=GROOVE, border=0, command=lambda: show("2")).place(x=80, y=374)

Button(root, text="1", font="Lucida 18 bold",
       pady=1, padx=23, background="White", relief=GROOVE, border=0, command=lambda: show("1")).place(x=160, y=374)

Button(root, text="+", font="ArialRounded 18",
       pady=3, padx=22, background="light grey", relief=GROOVE, border=0, command=lambda: show("+")).place(x=240, y=374)


Button(root, text="+/-", font="ArialRounded 18 bold",
       pady=1, padx=15, background="White", relief=GROOVE, border=0, command=lambda: show(f"-{eq}")).place(x=1, y=425)

Button(root, text="0", font="Lucida 18 bold",
       pady=1, padx=23, background="White", relief=GROOVE, border=0, command=lambda: show("0")).place(x=80, y=425)

Button(root, text=".", font="ArialRounded 18 bold",
       pady=1, padx=24, background="White", relief=GROOVE, border=0, command=lambda: show(".")).place(x=160, y=425)

Button(root, text="=", font="Lucida 18",
       pady=3, padx=25, background="#4599db", relief=GROOVE, border=0, command=lambda: calculate()).place(x=235, y=425)


root.mainloop()
