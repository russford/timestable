import tkinter
import random
from tkinter import filedialog, messagebox


class App(tkinter.Frame):
    def __init__(self, master):
        tkinter.Frame.__init__(self, master)
        self.master = master
        master.wm_title ("Times Table Test")

        frames, strings = zip(*[self.pack_frame(w) for w in [200, 50, 200, 50, 200]])

        self.str_num1 = strings[0]
        self.str_num2 = strings[2]
        self.str_result = strings[4]

        strings[1].set("x")
        strings[3].set("=")

        master.bind("<Key>", lambda e: self.keypress(e))
        master.bind("<Delete>", lambda e: self.clear(e))
        master.bind("<BackSpace>", lambda e: self.clear(e))
        master.bind("<Return>", lambda e: self.check(e))

        self.problems = []

        self.load_problem()

    def pack_frame (self, width):
        frame = tkinter.Frame(self.master, width=width, height=200)
        frame.pack(side="left", fill="both")
        string = tkinter.StringVar()
        label = tkinter.Label(frame, textvariable=string, font=("Helvetica", 48))
        label.place(relx=0.5, rely=0.5, anchor="center")
        return frame, string

    def keypress (self, event):
        if '0' <= event.char <= '9':
            try:
                s = self.str_result.get() + event.char
                n = int(s)
                self.str_result.set(s[-2:])
            except ValueError:
                pass

    def clear(self, event):
        self.str_result.set("")

    def update_total(self):
        correct = sum([n3 == n1*n2 for n1,n2,n3 in self.problems])
        total = len(self.problems)
        messagebox.showinfo("Progress", "{} / {} correct".format(correct, total))

    def check(self, event):
        n1 = int(self.str_num1.get())
        n2 = int(self.str_num2.get())
        n3 = int(self.str_result.get())

        self.problems.append((n1, n2, n3))
        self.update_total()
        self.load_problem()

    def load_problem(self):
        self.str_num1.set("{}".format(random.randint(1, 9)))
        self.str_num2.set("{}".format(random.randint(1, 9)))
        self.str_result.set("")

if __name__ == "__main__":
    root = tkinter.Tk()
    app = App(root)
    root.mainloop()



