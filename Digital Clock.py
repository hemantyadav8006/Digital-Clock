import sys
from tkinter import *
import time


def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200, tick)


root = Tk()
clock = Label(root, font=("time", 100, "bold"), bg="cyan")
clock.grid(row=100, column=100)
tick()
root.mainloop()

input()
