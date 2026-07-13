import tkinter 
import tkinter.messagebox
import time
screen=tkinter.Tk()
hour=tkinter.IntVar()
minutes=tkinter.IntVar()
seconds=tkinter.IntVar()
hour.set("00")
minutes.set("00")
seconds.set("00")
def start():
    response=int(entry1.get())   
    response2=int(entry2.get())
    response3=int(entry3.get())  
    ts=response*3600
    ts1=response2*60
    ts2=response3
    totalseconds=ts+ts1+ts2
    while totalseconds>0:
        totalseconds=totalseconds-1
        print(totalseconds)
        time.sleep(1)
        hr=totalseconds//3600
        m=totalseconds%3600//60
        s=totalseconds%60
        hour.set(hr)
        minutes.set(m)
        seconds.set(s)
        screen.update()
    
    tkinter.messagebox.showinfo("timer is up" , "THE TIMER IS DONE")

screen.geometry("500x200")

screen.title("Counter Stopwatch")
entry1=tkinter.Entry(screen,textvariable=hour)
entry2=tkinter.Entry(screen,textvariable=minutes)
entry3=tkinter.Entry(screen,textvariable=seconds )
button1=tkinter.Button(screen,text="set time countdown",command=start)

button1.grid(column=3,row=3)
entry1.grid(column=2,row=1)
entry2.grid(column=3,row=1)
entry3.grid(column=4,row=1)











screen.mainloop()