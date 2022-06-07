from tkinter import *
import time
# ============== settings ==============
window = Tk()
window.geometry("500x300")
window.resizable(width=False, height=False)
window.configure(bg='white smoke')
windowTitle = window.title("Clock")
# ============== Frames ==============
f1 = Frame(window, width=500, height=100)
f1.pack(side=TOP)


f2 = Frame(window, width=500, height=100)
f2.pack(side=TOP)

f3 = Frame(window, width=500, height=100)
f3.pack(side=BOTTOM)
# ============== Labels and Functions ==============


def date_text():
    date = time.strftime("%A")
    l1.config(text=date)
    l1.after(1000, date_text)


l1 = Label(f1, text="", font=("Mongolian Baiti", 20), fg="black")
date_text()
l1.pack()


def clock_text():
    h = time.strftime("%H")
    m = time.strftime("%M")
    s = time.strftime("%S")
    ampm = time.strftime("%p")
    final = f"{h}:{m}:{s} {ampm}"
    l2.after(1000, clock_text)
    l2.config(text=final)


l2 = Label(f2, text="", font=("Mongolian Baiti", 40), fg="black")
clock_text()
l2.pack(pady=30)


def zone_text():
    zone = time.strftime("%Z")
    l3.config(text=zone)
    l3.after(1000, zone_text)


l3 = Label(f3, text="", font=("Times New Roman", 20), fg="black")
zone_text()
l3.pack(pady=20)

window.mainloop()