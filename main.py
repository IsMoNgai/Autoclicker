from pynput.keyboard import Controller
import time
from tkinter import *
from tkinter import messagebox

def process():
    messagebox.showinfo("open the window you want NOW")
    time.sleep(5)
    t = True
    while t == True:
        keyboard.press(key1.get())
        time.sleep(1)
        keyboard.press(key2.get())
        time.sleep(1)
        keyboard.press(key3.get())
        time.sleep(1)

keyboard = Controller()

win = Tk()
win.geometry("400x250+800+300")
win.resizable(height=False, width=False)
win.title("Keypresser")
win.config(bg="#323232")

nothing = Label(win, text=" ", bg="#323232", fg="skyblue")

T = Label(win, text="Type in the key that you want it becomes a automatic key", bg="#323232", fg="skyblue")

key_1 = Label(win, text="The Fisrt Key", bg="#323232", fg="white")

key1 = Entry(win)
key1.get()

key_2 = Label(win, text="The Second Key", bg="#323232", fg="white")

key2 = Entry(win)
key2.get()

key_3 = Label(win, text="The Third Key", bg="#323232", fg="white")

key3 = Entry(win)
key3.get()

GB = Button(win, text="Start", command=process)

end = Button(win, text="END", command="break")

reminder = Label(win, text="ATTENTION: after you click the start button", bg="#323232", fg="white")

reminder2 = Label(win, text="          load the window you want immediately", bg="#323232", fg="white")

T.place(x=40, y=0)
key_1.place(x=150, y=20)
key1.place(x=130, y=40)
key_2.place(x=150, y=60)
key2.place(x=130, y=80)
key_3.place(x=150, y=110)
key3.place(x=130, y=130)
reminder.place(x=60, y=160)
reminder2.place(x=100, y=180)
GB.place(x=165, y=210, height=40, width=60)
end.place(x=280, y=210, height=40, width=60)


mainloop()
