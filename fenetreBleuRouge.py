"""
Nom exercice : Fenêtre bleu et rouge
Date : 10.11.2023
Auteur : ELod Arifi
"""

from tkinter import *

#Fonctions
def toBlue():
    global window, clcClicks
    window.configure(bg='blue')

    clcClicks += 1

def toRed():
    global window, clcClicks
    window.configure(bg='red')

    clcClicks += 1

def toHighLeft():
    global btnHighLeft, pox, poy, window, clcClicks
    pox = -10
    poy = 0
    window.geometry('+{}+{}'.format(pox,poy))

    clcClicks += 1

def toHighRight():
    global btnHighRight, pox, poy, window, clcClicks
    pox = 1025
    poy = 0
    window.geometry('+{}+{}'.format(pox,poy))

    clcClicks += 1

def toUnderLeft():
    global btnUnderLeft, pox, poy, window, clcClicks
    poy = 250
    pox = 0
    window.geometry('+{}+{}'.format(pox,poy))

    clcClicks += 1

def toUnderRight():
    global btnUnderRight, pox, poy, window, clcClicks
    poy = 250
    pox = 1025
    window.geometry('+{}+{}'.format(pox,poy))

    clcClicks += 1


def toMid():
    global btnToMid, pox, poy, window, clcClicks

    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    pox = (screenwidth / 2) - (width / 2)
    poy = (screenheight / 2) - (height / 2)
    window.geometry("%dx%d+%d+%d" % (width, height, pox, poy))
    window.resizable(False, False)

    clcClicks += 1


def toStats():
    global btnStats, window, pox, poy, clcClicks

    #Création de la nouvelle fenêtre
    windowStat = Tk()
    windowStat.config(width=200, height=200)

    #Placement de la fenêtre
    poy = 0
    pox = 1325
    windowStat.geometry('+{}+{}'.format(pox, poy))
    windowStat.title("Stats")

    #Label
    showStats = Label(windowStat, text=f"Vous avez appuyé : {clcClicks} fois")
    showStats.pack()




def exitWindow():
    global btnToExit
    window.destroy()


#Variables
pox = 0
poy = 0

clcClicks = 0

width = 500
height = 500

window = Tk()

#Cette partie permet de lancer le programme au millieu de l'écran
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
x = (screenwidth / 2) - (width / 2)
y = (screenheight / 2) - (height / 2)
window.geometry("%dx%d+%d+%d" % (width, height, x, y))
window.resizable(False, False)

window.title("Fenêtre")


#Bouttons

btnHighLeft = Button(window, text="Haut/Gauche", command=toHighLeft)
btnHighRight = Button(window, text="Haut/Droit", command=toHighRight)
btnUnderLeft = Button(window, text="Bas/Gauche", command=toUnderLeft)
btnUnderRight = Button(window, text="Bas/Droit", command=toUnderRight)
btnToMid = Button(window, text="Centre", command=toMid)

btnToBlue = Button(window, text="Bleu", command=toBlue)
btnToRed = Button(window, text="Rouge", command=toRed)

btnStats = Button(window, text="stats", command=toStats)
btnToExit = Button(window, text="Quitter", command=exitWindow)

#Packs
btnHighLeft.place(x = 0, y = 0)
btnHighRight.place(x = 431, y = 0)
btnUnderLeft.place(x = 0, y = 474)
btnUnderRight.place(x = 439, y = 474)
btnToMid.place(x = 233, y = 180)

btnToBlue.place(x = 238, y = 70)
btnToRed.place(x = 233, y = 140)

btnStats.place(x = 238, y = 300)
btnToExit.place(x = 232, y = 250)


window.mainloop()
