"""
Nom exercice : Créer une fênetre avec quelque label sans fonction
Date : 29.11.2023
Auteur : ELod Arifi
"""

import tkinter
from tkinter import *


#Starter Page
window = Tk()


#Variables


#Frame
frame1 = Frame(window)
frame1.pack(fill = "x")

frame2 = Frame(window)
frame2.pack(fill = "x")

frame3 = Frame(window)
frame3.pack(fill = "x")

frame4 = Frame(window)
frame4.pack(fill = "x")

#Labels
label1 = Label(frame1, text="Bonjours a: ")
label2 = Label(frame2, text="Bonjour b: ")
label3 = Label(frame3, text="Bonjour c: ")

#Entrys
entry1 = Entry(frame1)
entry2 = Entry(frame2)
entry3 = Entry(frame3)

#Buttons
button1 = Button(frame4, text="Au revoir1")
button2 = Button(frame4, text="Au revoir2")

#Affichage
entry1.pack(side=RIGHT)
label1.pack(side=RIGHT)

entry2.pack(side=RIGHT)
label2.pack(side=RIGHT)

entry3.pack(side=RIGHT)
label3.pack(side=RIGHT)

button2.pack(side=RIGHT)
button1.pack(side=RIGHT)

window.mainloop()