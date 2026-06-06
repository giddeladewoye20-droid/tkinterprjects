import tkinter 
import calendar
import random 
computerscore=0
playerscore=0
screen=tkinter.Tk()
screen.geometry("670x670")
screen.title("PAQUETA CRISPS")
list=["rock", "paper", "scissors"]
def confirm(playerselected):
   global playerscore
   global computerscore
   computerselected=random.choice(list)
   label3.config(text="You selected : "+ playerselected)
   label4.config(text="Computer selected : "+ computerselected)
   if playerselected=="rock" and computerselected=="rock":
      playerscore=playerscore+0 
      computerscore=computerscore+0 
      label7.config(text="Draw")
    

   if playerselected=="rock" and computerselected=="paper":
        playerscore=playerscore+0 
        computerscore=computerscore+1
        label7.config(text="Computer wins")


   if playerselected=="rock" and computerselected=="scissors":
      playerscore=playerscore+1 
      computerscore=computerscore+0 
      label7.config(text="You win")


   if playerselected=="scissors" and computerselected=="rock":
      playerscore=playerscore+0 
      computerscore=computerscore+1
      label7.config(text="Computer wins")


   if playerselected=="scissors" and computerselected=="scissors":
      playerscore=playerscore+0 
      computerscore=computerscore+0 
      label7.config(text="Draw")

   if playerselected=="scissors" and computerselected=="paper":
      playerscore=playerscore+1 
      computerscore=computerscore+0 
      label7.config(text="You win")



   if playerselected=="paper" and computerselected=="paper":
      playerscore=playerscore+0 
      computerscore=computerscore+0 
      label7.config(text="Draw")


   if playerselected=="paper" and computerselected=="rock":
      playerscore=playerscore+1 
      computerscore=computerscore+0 
      label7.config(text="You win")
    
    
   if playerselected=="paper" and computerselected=="scissors":
      playerscore=playerscore+0 
      computerscore=computerscore+1
      label7.config(text="Computer wins")
    
   label5.config(text=" player score: " + str(playerscore) )
   label6.config(text=" computer score: " + str(computerscore) )
    
    
        
    
     

    

label1=tkinter.Label(screen,text="Rock paper Scissors")
button1=tkinter.Button(screen,text="Rock",command=lambda:confirm("rock"))
button2=tkinter.Button(screen,text="Paper",command=lambda:confirm("paper"))
button3=tkinter.Button(screen,text="Scissors", command=lambda:confirm("scissors"))
label2=tkinter.Label(screen,text="Your options: ")
label3=tkinter.Label(screen,text="You selected: ")
label4=tkinter.Label(screen,text="Computer selected: ")
label5=tkinter.Label(screen,text= "player score: ")
label6=tkinter.Label(screen,text= "computer score: ")
label7=tkinter.Label(screen,text= "")

label1.grid(row=1,column=2)
label7.grid(row=2,column=2)
label2.grid(row=2,column=1)
button2.grid(row=3,column=2)
button1.grid(row=3,column=1)
button3.grid(row=3,column=3)
label3.grid(row=4,column=2)
label4.grid(row=5,column=2)
label5.grid(row=4,column=3)
label6.grid(row=5,column=3)



















screen.mainloop()