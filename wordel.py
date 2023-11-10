#Wordle v1
#11.01.2023
#Elod Arifi
import random
from tkinter import *

window = Tk()

#Variable
width = 400
height = 450
letter = 0
wordlist = []

#Prendre liste
with open("lb_fr.txt") as a:
    for e in a:
        wordlist.append(e)

word = random.choice(wordlist)

nbofLetter = len(word)

#Fenêtre au millieu
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
x = (screenwidth / 2) - (width / 2)
y = (screenheight / 2) - (height / 2)
window.geometry("%dx%d+%d+%d" % (width, height, x, y))
window.resizable(False, False)
window.title("Wordle")

#Frames
oneF = Frame(window)
twoF = Frame(window)
threeF = Frame(window)
fourF = Frame(window)
fiveF = Frame(window)
sixF = Frame(window)
sevenF = Frame(window)

for i in range(nbofLetter):
    Entry(threeF, width=5).pack(side=LEFT)

#Label
topLabel = Label(oneF, text="Wordle Game", font="Arial 20")

#Packs
topLabel.pack()
oneF.pack()
twoF.pack()
threeF.pack()




window.mainloop()
