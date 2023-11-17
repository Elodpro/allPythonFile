"""
Nom exercice : Score match
Date : 17.11.2023
Auteur : ELod Arifi
"""
from tkinter import *


window = Tk()

#Fonctions




#Variables
nbSetsUs = 0
nbPtsUs = 0

nbSetsNew = 0
nbPtsNew = 0

width = 500
height = 500
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
x = (screenwidth / 2) - (width / 2)
y = (screenheight / 2) - (height / 2)
window.geometry("%dx%d+%d+%d" % (width, height, x, y))
window.resizable(False, False)

window.title("Fenêtre")


#Frames
frame1 = Frame(window)
frame1.pack()

frame2 = Frame(window)
frame2.pack()

frame3 = Frame(window)
frame3.pack()


#Labels
nbOfSetsLb = Label(frame1, text="Nombre de sets ")
entrySets = Entry(frame1)

nbOfPtsLb = Label(frame1, text="Nombre de points ")
entryPts = Entry(frame1)

lcl = Label(frame2, text="Local:")
setsTxt1 = Label(frame2, text=f"Sets: {nbSetsUs}")
ptsTxt1 = Label(frame2, text=f"Points: {nbPtsUs}")
plusBtn1 = Button(window, text="+", fg="green")
minusBtn1 = Button(window, text="-", fg="red")


#Places

#FirstFrame
nbOfSetsLb.pack()
entrySets.pack()
nbOfPtsLb.pack()
entryPts.pack()

#SecondFrame
lcl.pack()
setsTxt1.pack()
ptsTxt1.pack()

window.mainloop()