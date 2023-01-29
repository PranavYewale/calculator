import tkinter as tk
import tkinter.messagebox as msg
import time

COLOR1 = "#e6e6e6"
COLOR2 = "light grey"
COLOR3 = "white"
COLOR4 = ''
FONT = "ArialRounded 18 bold"
FONT1 = 'BahnschriftSemiLightSemiConde 18 bold'
FONT2 = "ErasLightITC 15 "
FONT3 = "ErasLightITC 18 bold "
FONT4 = "Lucida 18 bold"
FONT5 = "ArialRounded 18"
RELIEF = 'groove'
DEFAULT_BORDER_VALUE = 0


class Calculator:

    def __init__(self) -> None:
        eq = ""
        resul = ""
        self.window = tk.Tk()
        self.window.geometry("317x475+600+200")
        self.window.title("Calculator")
        self.window.iconbitmap("py.ico")
        self.window.config(bg="#e6e6e6")
        self.window.minsize(width=317, height=475)
        self.expression = ''
        self.total_expression = ''
        self.label1 = self.create_display_frame1_and_label1()
        self.label2 = self.create_display_frame2_and_label2()
        self.eq = eq
        self.resul = resul

    def change(self):
        return self.window.geometry("317x475+-10+-80")

    def rechange(self):
        return self.window.geometry("317x475+600+200")

    def show(self, value):

        self.eq += value
        return self.label1.config(text=self.eq), self.label2.config(text=self.eq)

    def save(self):
        F = open("History.txt", "a")
        F.write(f" {time.asctime(time.localtime())}{self.eq,self.resul}\n")
        F.close()
        msg.showinfo("Done", "Saved")

    def clear(self):
        self.eq = ""
        return self.label1.config(text=self.eq), self.label2.config(text=self.eq)

    def none(self):
        msg.showinfo("Coming Soon..", "This Feature Does'nt Exists")

    def calculate(self):

        if self.eq != "":
            try:
                self.resul = eval(self.eq)
            except:
                self.resul = "Error"
                self.eq = ""
        self.label2.config(text=self.resul)

    def create_display_frame1_and_label1(self):
        frame1 = tk.Frame(self.window)
        frame1.place(x=15, y=50)
        label1 = tk.Label(frame1, text="", background="#e6e6e6",
                          font="Lucida 20 bold", border=0, fg="grey")
        label1.pack(anchor="e")

        return label1

    def create_display_frame2_and_label2(self):
        frame2 = tk.Frame(self.window)
        frame2.place(x=10, y=80)
        label2 = tk.Label(frame2, text="",
                          background="#e6e6e6", font="Lucida 40 bold", border=0)
        label2.pack(anchor='e')

        return label2

    def create_top_buttons(self):
        icons = ['≡', '⇱', '↺']
        valsx = [0, 160, 244]
        valsy = [0, 0, 0]
        icommand = [self.none, self.change, self.save]
        tk.Label(self.window, text="Standard ", font="BahnschriftSemiLightSemiConde 18 bold",
                 pady=1, padx=1, background="#e6e6e6", relief=RELIEF, border=0).place(x=35, y=7)
        top_buttons = []
        for i in range(3):
            button = tk.Button(
                self.window, text=icons[i], padx=1, pady=1, bg=COLOR1, font=FONT, relief=RELIEF, border=0, command=icommand[i])
            button.place(x=valsx[i], y=valsy[i])
            top_buttons.append(button)

        top_buttons[0].config(font="BahnschriftSemiLightSemiConde 18 bold")
        top_buttons[1].config(font="Lucida 18 ")
        top_buttons[2].config(font="ArialRounded 18 ", pady=3, padx=21)
        return top_buttons

    def give_command_to_top_buttons(self):
        pass

    def create_digit_buttons(self):
        icons = ['%', 'CE', 'C', "↻", '1/x', 'x²', '√x', "÷", "9", "8",
                 "7", "x", "6", "5", "4", '–', "3", "2", "1", "+", "+/-", "0", ".", "="]
        valsx = [0, 80, 160, 240, 1, 80, 160, 240, 1, 80, 160,
                 240, 1, 80, 160, 240, 1, 80, 160, 240, 1, 80, 160, 235]
        valsy = [170, 170, 170, 170, 221, 221, 221, 221, 272, 272, 272,
                 272, 323, 323, 323, 323, 374, 374, 374, 374, 425, 425, 425, 425]
        pad_x = [21, 19, 21, 22, 18, 21, 19, 22, 23, 23, 23,
                 24, 23, 23, 23, 23, 23, 23, 23, 22, 15, 23, 24, 25]
        pad_y = [1, 7, 1, 2, 6, 3, 3, 1, 1, 1, 1,
                 3, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1, 3]
        ivcommand = [lambda: self.show("%"), lambda: self.clear(), lambda: self.clear(), self.rechange, lambda: self.show("1/"), lambda: self.show("**2"), lambda:  self.show("**0.5"), lambda:  self.show("/"), lambda: self.show("9"), lambda: self.show("8"), lambda:  self.show("7"), lambda: self.show(
            "*"), lambda: self.show("6"), lambda: self.show("5"), lambda: self.show("4"), lambda: self.show("-"), lambda:  self.show("3"), lambda: self.show("2"), lambda: self.show("1"), lambda: self.show("+"), None, lambda:  self.show("0"), lambda: self.show("."), lambda: self.calculate()]
        buttons = []
        for i in range(24):
            button = tk.Button(
                self.window, text=icons[i], padx=pad_x[i], pady=pad_y[i], bg=COLOR3, font=FONT, relief=RELIEF, border=0, command=ivcommand[i])
            button.place(x=valsx[i], y=valsy[i])
            buttons.append(button)
        buttons[0].config(font=FONT, bg=COLOR2)
        buttons[1].config(font=FONT2, bg=COLOR2)
        buttons[2].config(font=FONT3, bg=COLOR2)
        buttons[3].config(font=FONT1, bg=COLOR2)
        buttons[4].config(font="ErasLightITC 16", bg=COLOR2)
        buttons[5].config(font=FONT5, bg=COLOR2)
        buttons[6].config(font="ArialRounded 18", bg=COLOR2)
        buttons[7].config(bg=COLOR2)
        buttons[8].config(font=FONT4)
        buttons[9].config(font=FONT4)
        buttons[10].config(font=FONT4)
        buttons[11].config(font=FONT5, bg=COLOR2)
        buttons[15].config(font=FONT5, bg=COLOR2)
        buttons[19].config(font=FONT5, bg=COLOR2)
        buttons[23].config(font=FONT5, bg="#4599db")

        return buttons

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calculator = Calculator()
    calculator.create_display_frame1_and_label1()
    calculator.create_display_frame2_and_label2()
    calculator.create_top_buttons()
    calculator.create_digit_buttons()
    calculator.run()
