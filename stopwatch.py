import tkinter 
screen=tkinter.Tk()
hour=tkinter.IntVar()
minutes=tkinter.IntVar()
seconds=tkinter.IntVar()
def start():
    response=int(entry1.get())  
    response2=int(entry2.get())
    response3=int(entry3.get())  

     

screen.geometry("500x200")
screen.title("Counter Stopwatch")
entry1=tkinter.Entry(screen)
entry2=tkinter.Entry(screen)
entry3=tkinter.Entry(screen)
button1=tkinter.Button(screen,text="set time countdown")

button1.grid(column=3,row=3)
entry1.grid(column=2,row=1)
entry2.grid(column=3,row=1)
entry3.grid(column=4,row=1)












screen.mainloop()