import tkinter,tkinter.messagebox
import random
screen=tkinter.Tk()
number=random.randint(1,20)
def function1():
    response=entry1.get() 
    tkinter.messagebox.showinfo("guess the number game","Hi " +  response  + " Im thinking of a number between 1 and 20, Try guess it ")
def function2():
    response1=int(entry2.get())
    if number==response1:
        tkinter.messagebox.showinfo("guess the number game","You have got it!!")
    elif number<response1:
        tkinter.messagebox.showinfo("guess the number game","My number is lower")
    elif number>response1:
        tkinter.messagebox.showinfo("guess the number game","My number is higher")
    
         
    

    


screen.geometry("670x670")
screen.title("PAQUETA CRISPS")
label1=tkinter.Label(screen,text="Welcome to our game ")
label3=tkinter.Label(screen,text="Take a guess:  ")
entry2=tkinter.Entry(screen)
label2=tkinter.Label(screen,text="Whats your name?")
entry1=tkinter.Entry(screen)
button1=tkinter.Button(screen,text="Ok",command=function1)
button2=tkinter.Button(screen,text="Guess",command=function2)
label1.grid(row=1,column=2)
label2.grid(row=3,column=1)
entry1.grid(row=4,column=1)
button1.grid(row=4,column=3)
entry2.grid(row=7,column=2)
label3.grid(row=7,column=1)
button2.grid(row=7,column=4)













screen.mainloop()
