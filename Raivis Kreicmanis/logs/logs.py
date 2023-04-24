from tkinter import*
mansLogs=Tk()
mansLogs.title('Nosaukums')
mansLogs.geometry('300x300')
poga=Button(mansLogs,text='Sveiki!',bg='black',fg='white')
poga.grid(row=1, column=0)
poga1=Button(mansLogs, text="Aizveriet",bg='green',fg='white', comand)
poga1.grid(row=10, column=2)

Label(mansLogs, text='Vārds').grid(row=2, column=0)
Label(mansLogs, text='Uzvārs').grid(row=3, column=0)
e1= Entry(mansLogs)
e1= Entry(mansLogs)

mansLogs.mainloop()