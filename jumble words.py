# -*- coding: utf-8 -*-
"""
Created on Sat May 25 23:55:49 2019

@author: ASUS
"""
import tkinter
from tkinter import *
import random
from random import shuffle
from tkinter import messagebox

JUMBLED, PLAINTEXT = 0, 1


tv_shows = [
    'Game of Thrones', 'Friends', 'How I Met Your Mother', 'Breaking Bad', 'Narcos', 'Flash', 'Arrow', 'Big Bang Theory',
    'Walking Dead', 'Agents Of Shield', 'Blue Planet 2', 'Legion', 'The Grand Tour', 'Band Of Brothers', 'Westworld'
    'Sherlock', 'The Punisher', 'True Detective', 'Daredevil', 'Luke Cage', 'Jessica Jones', 'Iron Fist', 'Stranger Things',
    'Rick and Morty', 'House of Cards', '13 Reasons Why', 'House MD', 'Castle', 'Doctor Who', 'Dexter', 'Suits'
]
def word_jumble(word):
    letters = list(word)

    shuffle(letters)

    return "".join(letters)

def sentence_jumble(w):
    words = w.split()

    shuffle(words)

    return " ".join(word_jumble(word) for word in words)

def res():
    global jumble
    lbl.config(text="" + jumble[JUMBLED])
    e1.delete(0,END)
    
    
    
def start_game():
    global jumble

    e1.focus_set()

    jumble = jumble_list.pop()

    lbl.config(text="" + jumble[JUMBLED])
    
    
def score_game():
    global score

    if e1.get().lower() == jumble[PLAINTEXT].lower():
        e1.delete(0, END)

        score += 1
        score_display.config(text="Score - "+str(score))

        if jumble_list:
            score_display.after(500, start_game)
        else:
            main.unbind('<Return>')
            
        messagebox.showinfo("Success","This is a correct answer")
        res()
        
    else:
        messagebox.showerror("Error","This is not correct")
        e1.delete(0, END)
        score_display.after(500, start_game)








shuffle(tv_shows)

jumble_list = [(sentence_jumble(title), title) for title in tv_shows]

score = 0
jumble = None  # a tuple with (jumbled, plaintext)

root = tkinter.Tk()
root.geometry("350x400+400+300")
root.title("Play with Jumble")
root.configure(background="#000000")

lbl = Label(
    root,
    text = "Your here",
    font = ("Verdana", 18),
    bg = "#000000",
    fg = "#ffffff",
)
lbl.pack(pady=30,ipady=10,ipadx=10)




ans1 = StringVar()
e1 = Entry(
    root,
    font = ("Verdana", 16),
    textvariable = ans1,
)
e1.pack(ipady=5,ipadx=5)
e1.focus_set()

btncheck = Button(
    root,
    text = "Check",
    font = ("Comic sans ms", 16),
    width = 16,
    bg = "#4C4B4B",
    fg = "#6ab04c",
    relief = GROOVE,
    command = score_game,
)
btncheck.pack(pady=40)


btnreset = Button(
    root,
    text = "Reset",
    font = ("Comic sans ms", 16),
    width = 16,
    bg = "#4C4B4B",
    fg = "#EA425C",
    relief = GROOVE,
    command = start_game,
)
btnreset.pack()

score_display = Button(
        root,
        text="Score",
        font=("Comic sans ms", 16),
        width=16,
        bg="#DFAF2B",
        fg="#218F76",
        relief = GROOVE,
)
score_display.pack(pady=20)
score_display.config(text="Score - " + str(score))


start_game()


root.mainloop()