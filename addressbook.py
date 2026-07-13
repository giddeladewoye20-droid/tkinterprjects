import tkinter 
screen=tkinter.Tk()
    

screen.geometry("500x200")
screen.title("PAQUETA CRISPS")
label1=tkinter.Label(screen,text="My address book")
label2=tkinter.Label(screen,text="Name: ")
label3=tkinter.Label(screen,text="Address: ")
label4=tkinter.Label(screen,text="Mobile: ")
label5=tkinter.Label(screen,text="Email: ")
label6=tkinter.Label(screen,text="Birthday: ")
entry2=tkinter.Entry(screen)
entry3=tkinter.Entry(screen)
entry4=tkinter.Entry(screen)
entry5=tkinter.Entry(screen)
entry6=tkinter.Entry(screen)

button1=tkinter.Button(screen,text="Open")


label1.grid(column=3,row=1)
button1.grid(column=5,row=1)
label2.grid(column=5,row=5)
label3.grid(column=5,row=7)
label4.grid(column=5,row=9)
label5.grid(column=5,row=11)
label6.grid(column=5,row=13) 
entry2.grid(column=6,columnspan=8,row=5)                     
entry3.grid(column=6,columnspan=8,row=7) 
entry4.grid(column=6,columnspan=8,row=9) 
entry5.grid(column=6,columnspan=8,row=11) 
entry6.grid(column=6,columnspan=8,row=13) 






























screen.mainloop()