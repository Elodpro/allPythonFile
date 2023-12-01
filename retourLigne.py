"""
Nom exercice : Retourne à la ligne les mots
Date : 01.12.2023
Auteur : ELod Arifi
"""

###############
#Importe
###############
from tkinter import *

###############
#Fonction
###############

def change_label():
    global lbl_change, txt_name

    old_message = lbl_change['text']

    new_message = txt_name.get()

    lbl_change.config(text=old_message + "\n"  + new_message)

    txt_name.delete(0, END)




###############
#Variable
###############
root = Tk()

root_width = 400
root_height = 400

###############
#Programe
###############

#Fenêtre
#calcul la taille de l'écrant
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#comande pour centre
center_x = int(screen_width/2 - root_width / 2)
center_y = int(screen_height/2 - root_height / 2)

#création de la fenetre
root.title("Changement de nombre")
root.geometry(f"{root_width}x{root_height}+{center_x}+{center_y}")

#Frame
#Création d'une frame pour le label et entry
frame1 = Frame(root)
frame1.pack()

#Création d'une frame pour le label qui change
frame2 = Frame(root)
frame2.pack()

#Label
#label fixe
lbl_name = Label(frame1,text="Entrez votre nom")
lbl_name.pack(side=LEFT)

#label change
lbl_change = Label(frame2,text="")
lbl_change.pack()

#Entry
#entry qui remplace le label
txt_name = Entry(frame1)
txt_name.pack(side=LEFT)

#botton qui change le label
bt_change = Button(frame2, text="Valider", command=change_label)
bt_change.pack()


#pour garder la fenetre ouverte
root.mainloop()