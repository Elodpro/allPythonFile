"""
Nom exercice : Score match
Date : 17.11.2023
Auteur : ELod Arifi
"""
from tkinter import *


window = Tk()

#Fonctions

def verifPtsWin():
    global nbPtsUs, howManyPts, ptsTxt1, nbSetsUs, setsTxt1, nbPtsNew, nbSetsNew, ptsTxt2, setsTxt2

    if nbPtsUs == howManyPts:
        nbSetsUs += 1
        setsTxt1.config(text=f"Sets: {nbSetsUs}")

        nbPtsUs = 0
        ptsTxt1.config(text=f"Points: {nbPtsUs}")

    elif nbPtsNew == howManyPts:
        nbSetsNew += 1
        setsTxt2.config(text=f"Sets: {nbSetsNew}")

        nbPtsNew = 0
        ptsTxt2.config(text=f"Points: {nbPtsNew}")

def verifSetsWin():
    global nbSetsUs, nbSetsNew, howManySets

    if nbSetsUs == howManySets:
        winLabel = Label(window, text=f"Le joueur 'Local' a gagné le match !")
        winLabel.place(x=22, y=150)

    elif nbSetsNew == howManySets:
        winLabel2 = Label(window, text=f"Le joueur 'invité' a gagné le match !")
        winLabel2.place(x=22, y=150)


def takeEntry():
    global howManySets, entrySets, howManyPts

    howManySets = entrySets.get()
    howManyPts = entryPts.get()

    howManyPts = int(howManyPts)
    howManySets = int(howManySets)

    print(f"nb sets: {howManySets}\nnb points: {howManyPts}")


def addPointsUs():
    global nbPtsUs, howManyPts, ptsTxt1, setsTxt1, nbSetsUs

    nbPtsUs += 1
    ptsTxt1.config(text=f"Points: {nbPtsUs}")
    verifPtsWin()
    verifSetsWin()


def addPointsNew():
    global nbPtsNew, howManyPts, ptsTxt2, setsTxt2, nbSetsNew

    nbPtsNew += 1
    ptsTxt2.config(text=f"Points: {nbPtsNew}")
    verifPtsWin()
    verifSetsWin()


def delPointsUs():
    global nbPtsUs, ptsTxt1

    nbPtsUs -= 1
    ptsTxt1.config(text=f"Points: {nbPtsUs}")
    verifPtsWin()
    verifSetsWin()

def delPointsNew():
    global nbPtsNew, ptsTxt2

    nbPtsNew -= 1
    ptsTxt2.config(text=f"Points: {nbSetsNew}")
    verifPtsWin()
    verifSetsWin()


#Variables
nbSetsUs = 0
nbPtsUs = 0

howManySets = 0
howManyPts = 0

nbSetsNew = 0
nbPtsNew = 0

width = 235
height = 200
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
x = (screenwidth / 2) - (width / 2)
y = (screenheight / 2) - (height / 2)
window.geometry("%dx%d+%d+%d" % (width, height, x, y))
window.resizable(False, False)

window.title("Score")


#Frames
frame1 = Frame(window,width=80)
frame1.grid()

frame2 = Frame(window, height=300, width=300)
frame2.grid()


#Labels
nbOfSetsLb = Label(frame1, text="Nombre de sets ")
entrySets = Entry(frame1)

nbOfPtsLb = Label(frame1, text="Nombre de points ")
entryPts = Entry(frame1)


#Sets, points etc du joueur local
lcl1 = Label(frame2, text="Local:")
plusBtn1 = Button(window, text="+", fg="green", command=addPointsUs)
minusBtn1 = Button(window, text="-", fg="red", command=delPointsUs)
setsTxt1 = Label(frame2, text=f"Sets: {nbSetsUs}")
ptsTxt1 = Label(frame2, text=f"Points: {nbPtsUs}")


#Sets, points etc du joueurs invité
lcl2 = Label(frame2, text="Local:")
plusBtn2 = Button(window, text="+", fg="green", command=addPointsNew)
minusBtn2 = Button(window, text="-", fg="red", command=delPointsNew)
setsTxt2 = Label(frame2, text=f"Sets: {nbSetsUs}")
ptsTxt2 = Label(frame2, text=f"Points: {nbPtsUs}")


#Prends la valeur des entrys
takeNbBtn = Button(window, text="Envoyer", command=takeEntry)


#Places

#FirstFrame
nbOfSetsLb.grid()
entrySets.grid(row = 0, column = 2)
nbOfPtsLb.grid()
entryPts.grid(row = 1, column = 2)

#SecondFrame
lcl1.grid(row = 4, column = 0)
setsTxt1.grid(row = 3, column = 0)
ptsTxt1.grid(row = 2, column = 0)
plusBtn1.place(x=69,y=110)
minusBtn1.place(x=89,y=110)

lcl2.grid(row = 4, column = 1)
setsTxt2.grid(row = 3, column = 1)
ptsTxt2.grid(row = 2, column = 1)
plusBtn2.place(x=120, y=110)
minusBtn2.place(x=140, y=110)

takeNbBtn.place(x=176, y=40)

window.mainloop()