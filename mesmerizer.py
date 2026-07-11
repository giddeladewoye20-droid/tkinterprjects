import tkinter 
screen=tkinter.Tk()

    

screen.geometry("500x200")
screen.title("PAQUETA CRISPS") 


label1=tkinter.Label(screen)
entry1=tkinter.Entry(screen)
label2=tkinter.Label(screen)
entry2=tkinter.Entry(screen)
button1=tkinter.Button(screen,text="delete")
button2=tkinter.Button(screen,text="open")
button3=tkinter.Button(screen,text="save")
button4=tkinter.Button(screen,text="add")
listbox=tkinter.Listbox(screen)

button1.grid(row=1,column=2)
button2.grid(row=1,column=1)
button3.grid(row=1,column=3)
button4.grid(row=2,column=3)
listbox.grid(row=3,column=1,columnspan=3)
entry1.grid(row=2,column=1,columnspan=2)


























screen.mainloop()