import tkinter 
screen=tkinter.Tk()
def confirm():
    response=entry1.get()  
    response2=entry2.get()
    if response=="Giddel":
    
     if response2=="ah2":
       print("correct")
    

screen.geometry("670x670")
screen.title("PAQUETA CRISPS")
label1=tkinter.Label(screen,text="Username")
entry1=tkinter.Entry(screen)
label2=tkinter.Label(screen,text="Password")
entry2=tkinter.Entry(screen)
button1=tkinter.Button(screen,text="Confirm",command=confirm)
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
button1.pack()
screen.mainloop()

