import tkinter 
import calendar
screen=tkinter.Tk()

def showcalendar():
    response=int(entry2.get())
    calendartext=calendar.calendar(response)
    screen2=tkinter.Tk()
    screen2.geometry("670x670")
    text=tkinter.Text(screen2)
    text.insert(tkinter.END,calendartext)
    text.pack()

screen.geometry("670x670")
screen.title("PAQUETA CRISPS")
label1=tkinter.Label(screen,text="Calendar",font=("Arial",40,"bold"),bg="red")
label2=tkinter.Label(screen,text="Enter year:",font=("comic style",20))
entry2=tkinter.Entry(screen)
button1=tkinter.Button(screen,text="Show calendar",command=showcalendar)
button2=tkinter.Button(screen,text="Exit")

label1.pack()
label2.pack()
entry2.pack()
button1.pack()
button2.pack

screen.mainloop()