from tkinter import *
from tkinter import ttk
from tkinter import messagebox

my_window = Tk()
my_list = ["Araignée", "Chat", "Cheval", "Chien", "Cobra", "Coccinelle", "Kangourou", "Perroquet", "Rat", "Ver de terre"]
my_listbox_in = Listbox(my_window, height=10)
my_listbox_in.grid(row=0, column=0, padx=10, pady=10)
my_listbox_out = Listbox(my_window, height=10)
my_listbox_out.grid(row=0, column=2, padx=(50), pady=10)

#Boucle affichant la liste
for itm in my_list:
    my_listbox_in.insert(END, itm)

#Fonction qui déplace tout à droite grace à un mouseevent
def dbl_click(event):
    for i in range(my_listbox_out.size()):
        my_listbox_in.insert(my_list.index(my_listbox_out.get(0)), my_listbox_out.get(0))
        my_listbox_out.delete(0)
    return event



#Fonction pour le boutton de haut qui envoie les itm à droite
def top_cmd():
    if my_listbox_in.curselection() == ():
        messagebox.showinfo("Vous n'avez rien séléctionné")
    # Index le numéro d'un élément de la liste le prend et l'insert à droite
    else:
        my_listbox_out.insert(my_list.index(my_listbox_in.get(ANCHOR)), my_listbox_in.get(ANCHOR))
        my_listbox_in.delete(ANCHOR)

#Fonction pour le boutton de bas qui envoie les tm à gauche
def bottom_cmd():
    if my_listbox_out.curselection() == ():
        messagebox.showinfo("Vous n'avez rien séléctionné")
    #Index le numéro d'un élément de la liste le prend et l'insert à gauche
    else:
        my_listbox_in.insert(my_list.index(my_listbox_out.get(ANCHOR)), my_listbox_out.get(ANCHOR))
        my_listbox_out.delete(ANCHOR)


btn1 = Button(my_window, text="===>",command=top_cmd ).place(x=140, y=30)
btn2 = Button(my_window, text="<===", command=bottom_cmd).place(x=140, y=126)

#MouseEvent pour cliquer dans la case gauche
my_listbox_in.bind("<Double-1>", dbl_click)

#MouseEvent pour cliquer dans la case droite
my_listbox_out.bind("<Double-1>", dbl_click)

mainloop()
