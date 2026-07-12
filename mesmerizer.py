import tkinter
import tkinter.filedialog 
screen=tkinter.Tk()

    

screen.geometry("500x200")
screen.title("PAQUETA CRISPS") 

def openfunc():
   ayrmimightjsbunhim=tkinter.filedialog.askopenfile()
   if ayrmimightjsbunhim != None:
       slidenyuckhim=ayrmimightjsbunhim.readlines()
       listbox.delete(0,tkinter.END)
       for item in slidenyuckhim:
           listbox.insert(tkinter.END,item)


def deletefunc():
   index=listbox.curselection()
   listbox.delete(index)

def savefunc():
    dkpassmethesuttin=tkinter.filedialog.asksaveasfile()
    if dkpassmethesuttin != None:
        for item in listbox.get(0,tkinter.END):
            print(item,file=dkpassmethesuttin)

def addfunc():
   addresponse=entry1.get()
   if addresponse !="":
       listbox.insert(tkinter.END,addresponse)
       entry1.delete(0,tkinter.END)


entry1=tkinter.Entry(screen)
button1=tkinter.Button(screen,text="delete",command=deletefunc)
button2=tkinter.Button(screen,text="open",command=openfunc)
button3=tkinter.Button(screen,text="save",command=savefunc)
button4=tkinter.Button(screen,text="add",command=addfunc)
listbox=tkinter.Listbox(screen)

button1.grid(row=1,column=2)
button2.grid(row=1,column=1)
button3.grid(row=1,column=3)
button4.grid(row=2,column=3)
listbox.grid(row=3,column=1,columnspan=3)
entry1.grid(row=2,column=1,columnspan=2)


























screen.mainloop()