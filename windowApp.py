from tkinter import*

# Variables
localSets = 0
localPoints = 0
invitSets = 0
invitPoints = 0


window = Tk()
window.geometry()
frame1 = Frame()
frame1.pack()
label = Label(frame1, text="nombre de sets",)
label.pack(side=LEFT)
entry = Entry(frame1)
entry.pack(side=LEFT)

frame2 = Frame()
frame2.pack()
label2 = Label(frame2, text="nombre de points",)
label2.pack(side=LEFT)
entry2 = Entry(frame2)
entry2.pack(side=LEFT)

frame3 = Frame()
frame3.pack()

frame4 = Frame(frame3)
frame4.pack(side=LEFT)
label3 = Label(frame4, text="local:")
label3.pack(side=TOP)
label4 = Label(frame4, text=f"sets: {localSets}")
label4.pack(side=TOP)
label5 = Label(frame4, text=f"points: {localPoints}")
label5.pack(side=TOP)

frame5 = Frame(frame3)
frame5.pack(side=LEFT)
label6 = Label(frame5, text="invité:")
label6.pack(side=TOP)
label7 = Label(frame5, text=f"sets: {invitSets}")
label7.pack(side=TOP)
label8 = Label(frame5, text=f"points: {invitPoints}")
label8.pack()

frame6 = Frame(frame4)
frame6.pack()
button1 = Button(frame6, text="+", fg="green")
button1.pack(side=LEFT)
button2 = Button(frame6, text="-", fg="red")
button2.pack(side=LEFT)

frame7 = Frame(frame5)
frame7.pack()
button1 = Button(frame7, text="+", fg="green")
button1.pack(side=LEFT)
button2 = Button(frame7, text="-", fg="red")
button2.pack(side=LEFT)


window.title("score")
window.mainloop()
