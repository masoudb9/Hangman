import sys
import os
import random
from tkinter import Tk, Label, Button, messagebox, Entry

list3 = ['blue', ' have', 'gold', 'book', 'ball', 'maze', 'busy', 'flat', 'rose', 'roof', 'swim', 'comb', 'fork',
         'red', 'yes', 'app', 'hen', 'egg', 'row', 'raw', 'day', 'bad', 'now', 'zoo', 'tea', 'sea', 'see', 'fed',
         'black', 'white', 'brown', 'water', 'chair', 'table', 'phone', 'young', 'zebra', 'score',  'tools', 'light',
         'ticket', 'cinema', 'window', 'python', 'random', 'choice', 'global', 'always', 'script', 'admire', 'effect']

num1 = random.choice(list3)
score = 50
score2 = 0


def click1():
    global score
    global score2
    var = txt.get()
    if var != num1:
        score = score - 5
        label.config(text=f"Score: {score}", background='lightpink', foreground='black')
        messagebox.showinfo("Notice", "Wrong Guess Try Again")
        if score == 0:
            messagebox.showinfo("Notice", "Game over")
            window.destroy()
    if var == num1:
        score = score + 5
        b1.destroy()
        label.config(text=f"Score: {score}", background='lightgreen', foreground='black')
        messagebox.showinfo("Congratulation", "You Won The Game, Start a new game :)")
        window.minsize(280, 160)
        window.maxsize(280, 160)

def click2():
    global score
    score = score - 20
    label.config(text=f"Score: {score}", background='lightpink', foreground='black')
    messagebox.showinfo("Hint", f"first letter:{num1[0]}  last letter:{num1[-1]}")
    b2.destroy()



def new_game():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def click3():
    window.destroy()


window = Tk()
window.title("|^_^| HangMan")
window.maxsize(280, 230)
window.minsize(280, 230)
Label(window, text="there are different words in this game :)".title(), background='gold', foreground='black',
      width=35).pack(pady=5)
txt = Entry(window, width=45, background='lightgrey', foreground='black')
txt.pack(pady=5)
label = Label(window, text=f'Score: {score}',bg='lightpink')
label.pack()
b1 = Button(window, text="Check", background='green', foreground='black', width=35, command=click1)
b1.pack(pady=5)
b2 = Button(window, text="Hint(1)", background='yellow', foreground='black', width=35, command=click2)
b2.pack(pady=5)
b2_3 = Button(window, text="New Game", background='skyblue', foreground='black', width=35, command=new_game)
b2_3.pack(pady=5)
b3 = Button(window, text="Exit", background='lightgrey', foreground='black', width=35, border=2, command=click3)
b3.pack(pady=5)
window.mainloop()
