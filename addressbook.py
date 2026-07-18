import tkinter 
import tkinter.filedialog
screen=tkinter.Tk()
addressbox={}
def addfunc():
    response1=entry2.get()
    response2=entry3.get()
    response3=entry4.get()
    response4=entry5.get()
    response5=entry6.get()
    addressbox[response1]=[response2,response3,response4,response5]
    entry2.delete(0,tkinter.END)
    entry3.delete(0,tkinter.END)
    entry4.delete(0,tkinter.END)
    entry5.delete(0,tkinter.END)
    entry6.delete(0,tkinter.END)

def deletefunc():
   index=listbox.curselection()
   nameofpers=listbox.get(index)
   del addressbox[nameofpers]


def savefunc():
    dkpassmethesuttin=tkinter.filedialog.asksaveasfile()
    if dkpassmethesuttin != None:
        for item in listbox.get(0,tkinter.END):
            print(item,file=dkpassmethesuttin)



def openfunc():
   ayrmimightjsbunhim=tkinter.filedialog.askopenfile()
   if ayrmimightjsbunhim != None:
       slidenyuckhim=ayrmimightjsbunhim.readlines()
       listbox.delete(0,tkinter.END)
       for item in slidenyuckhim:
           listbox.insert(tkinter.END,item)





   









screen.geometry("500x300")
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
button2=tkinter.Button(screen,text="Delete")
button3=tkinter.Button(screen,text="Edit")
button4=tkinter.Button(screen,text="Update/Add")
button5=tkinter.Button(screen,text="Save")
listbox=tkinter.Listbox(screen)

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
button2.grid(column=3,row=15)
button3.grid(column=1,row=15)
button4.grid(column=7,row=15)
listbox.grid(column=1,row=5,rowspan=7)
button5.grid(column=3,row=17,columnspan=7)


























screen.mainloop()