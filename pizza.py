"""
Nom exercice : Estimation fictive de revenu imposable
Date : 06.12.2023
Auteur : ELod Arifi
"""
import tkinter
from tkinter import *
from tkinter.messagebox import showinfo



#Fonctions
def entryFalse():
    global tableLabel, tableEntry

    tableEntryGet = tableEntry.get()

    while not tableEntryGet.isdigit():
        showinfo(message="Vous devez saisir un numéro de table!")
        tableEntry.delete("0", END)
        tableEntryGet = 0


def commandeDone():
    global box1Check_bool, box2Check_bool, box3Check_bool, box4Check_bool, tableEntryGet

    res = f"Pour la {tableEntryGet}"

    if anchoisCheck == 0:
        ben


#Starter Page
window = Tk()
width = 350
height = 400
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
x = (screenwidth / 2) - (width / 2)
y = (screenheight / 2) - (height / 2)
window.geometry("%dx%d+%d+%d" % (width, height, x, y))
window.resizable(False, False)

window.title("Pizza")

#Frames
frameEntry = Frame(window)
frameEntry.pack(fill = "x")

#Entry
tableEntry = Entry(frameEntry)

#Variables
var = IntVar()

tableEntryGet = tableEntry.get()

box1Check_bool = BooleanVar()
box2Check_bool = BooleanVar()
box3Check_bool = BooleanVar()
box4Check_bool = BooleanVar()



framePrince = Frame(window)
framePrince.pack(fill="x", pady=10)


radioFrame = LabelFrame(framePrince, text="Pâtes")
radioFrame.pack(fill="x", expand="no", side=LEFT, padx=50)

checkBtnFrame = Frame(framePrince)
checkBtnFrame.pack(fill="x", side=RIGHT, padx= 50)

#Labels
tableLabel = Label(frameEntry, text="Table")

txtCommande = Label(window, text="Commande")





#RadioButtons..
extrafineCheck = Radiobutton(radioFrame, text="Extra-fine", variable=var, value=1)
extrafineCheck.pack(anchor=W)

fineCheck = Radiobutton(radioFrame, text="Fine", variable=var, value=2)
fineCheck.pack(anchor=W)

normalCheck = Radiobutton(radioFrame, text="Normal", variable=var, value=3)
normalCheck.pack(anchor=W)

epaisseCheck = Radiobutton(radioFrame, text="Epaisse", variable=var, value=4)
epaisseCheck.pack(anchor=W)


#CheckButtons
anchoisCheck = Checkbutton(checkBtnFrame, text="Anchois", variable=box1Check_bool, onvalue=True, offvalue=False)
anchoisCheck.pack(anchor=W)

capreCheck = Checkbutton(checkBtnFrame, text="Câpres", variable=box2Check_bool, onvalue=True, offvalue=False)
capreCheck.pack(anchor=W)

jambonCheck = Checkbutton(checkBtnFrame, text="Jambon", variable=box3Check_bool, onvalue=True, offvalue=False)
jambonCheck.pack(anchor=W)

crevetteCheck = Checkbutton(checkBtnFrame, text="Crevettes", variable=box4Check_bool, onvalue=True, offvalue=False)
crevetteCheck.pack(anchor=W)

#Buttons
commandBtn = Button(window, text="Commander", command=entryFalse)


#Displays
tableLabel.pack(side=LEFT)
tableEntry.pack(side=LEFT)

commandBtn.place(x=240, y=170)

txtCommande.place(x=50, y=180)


window.mainloop()