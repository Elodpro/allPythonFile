"""
Nom exercice : Estimation fictive de revenu imposable
Date : 24.11.2023
Auteur : ELod Arifi
"""
import tkinter
from tkinter import *



#Fonctions

def takeEntrys():
    global annualRev_Entry, familyCoef_Entry, youngDeduc_Entry, transportDeduc_Entry, loyalDiscount_Entry
    global revenu, coFamilial, deducJeune, deducTransport, rabaisFidelite
    global box1Check, box2Check, box3Check



    revenu = annualRev_Entry.get()
    coFamilial = familyCoef_Entry.get()

    annualRev_Entry.delete("0", "end")

    print(box1)

    if box1Check_bool.get() :

        deducJeune = youngDeduc_Entry.get()
        print(deducJeune)

    if box2Check_bool.get() :
        deducTransport = transportDeduc_Entry.get()
        print(deducTransport)
    if box3Check_bool.get() :
        rabaisFidelite = loyalDiscount_Entry.get()
        print(rabaisFidelite)



def allCalcul():
    global revenu, coFamilial, deducJeune, deducTransport, rabaisFidelite
    global clc1, clc2, clc3, clc4

    #Divise le revenu brut par le coefficient familial
    clc1 = revenu / coFamilial


def finalExecute():

    print()



#Starter Page
window = Tk()
box1Check_bool = BooleanVar()
box2Check_bool = BooleanVar()
box3Check_bool = BooleanVar()
width = 235
height = 400
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
x = (screenwidth / 2) - (width / 2)
y = (screenheight / 2) - (height / 2)
window.geometry("%dx%d+%d+%d" % (width, height, x, y))
window.resizable(False, False)

window.title("Déductions")


#Variables
revenu = 0
coFamilial = 0
deducJeune = 0
deducTransport = 0
rabaisFidelite = 0

clc1 = 0
clc2 = 0
clc3 = 0
clc4 = 0

box1Check = False
box2Check = False
box3Check = False


#Frames
topFrame = Frame(window)
topFrame.grid()

invisibleFrame = Frame(window)
invisibleFrame.grid()

midFrame = Frame(window)
midFrame.grid()

#Labels
annualRev = Label(topFrame, text="Revenu annuel brut")
familyCoef = Label(topFrame, text="Coefficient familial")

invisibleLabel = Label(invisibleFrame, text="")

youngDeduc = Label(midFrame, text="Déduction jeune")
transportDeduc = Label(midFrame, text="Déduction transport")
loyalDiscount = Label(midFrame, text="Rabais fidélité (%)")


#Entrys
annualRev_Entry = Entry(topFrame)
familyCoef_Entry = Entry(window, width=5)

youngDeduc_Entry = Entry(window, width=5)
transportDeduc_Entry = Entry(window, width=5)
loyalDiscount_Entry = Entry(window, width=5)

#ChecksBoxs
box1 = Checkbutton(midFrame, variable=box1Check_bool, onvalue=True,offvalue=False)
box2 = Checkbutton(midFrame, variable=box2Check_bool, onvalue=True,offvalue=False)
box3 = Checkbutton(midFrame, variable=box3Check_bool, onvalue=True,offvalue=False)

#Buttons
calculBtn = Button(window, text="Calcul", command=takeEntrys)



#Displays
annualRev.grid(row=0, column=0)
annualRev_Entry.grid(row=0, column=1)

familyCoef.grid(row=1, column=0)
familyCoef_Entry.place(x=199, y=23)

invisibleLabel.grid()

youngDeduc.grid(row=0, column=1)
youngDeduc_Entry.place(x=199, y=67)

transportDeduc.grid(row=1, column=1)
transportDeduc_Entry.place(x=199, y=92)

loyalDiscount.grid(row=2, column=1)
loyalDiscount_Entry.place(x=199, y=117)

box1.grid(row=0, column=0)
box2.grid(row=1, column=0)
box3.grid(row=2, column=0)

calculBtn.place(x=100, y=160)



window.mainloop()
