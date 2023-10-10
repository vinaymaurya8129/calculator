from tkinter import *
root=Tk()
def click(event):
    global Svariable
    text=event.widget.cget("text")
    if text=="=":
        if Svariable.get().isdigit():
            value=int(Svariable.get())
        else:
            try:
                value=eval(screen.get())
            except:
                value="error"
        Svariable.set(value)
        screen.update()
    elif text=="C":
        Svariable.set("")
        screen.update()
    elif text=="<":
        sl1=Svariable.get()
        sl2=sl1[-1]
        sl=sl1.replace(sl2,"")
        Svariable.set(sl)
    else:
        Svariable.set(Svariable.get()+text)
        screen.update()

root.geometry("376x402")
root.minsize(376, 402)
root.maxsize(376, 402)
root.title("Calculator")
try:
    root.wm_iconbitmap("cal.ico")
except:
    root.wm_iconbitmap("calculator\\cal.ico")

Svariable=StringVar()
Svariable.set("")
#display
screenFrame=Frame(root,background="grey")
screen=Entry(screenFrame,textvariable=Svariable,font="lucida 30 bold",bg="light blue",relief=GROOVE)
screen.pack(padx=8,pady=2,ipadx=10,ipady=4)
screenFrame.pack()

list1=['7','8','9','-','4','5','6','*','1','2','3','/']
list2=['0','.','+','C','<','=']
count1=len(list1)
count2=len(list2)
# buttons
increament=0
for i in range(3):
    buttonFrame=Frame(root)
    for j in range(4):
        button=Button(buttonFrame,text=str(list1[increament]),font="lucida 25 bold",bg="grey",width=4)
        button.pack(side=LEFT,ipadx=2,ipady=1)
        button.bind("<Button-1>",click)
        increament+=1
    buttonFrame.pack()  

increament=0
for i in range(2):
    buttonFrame=Frame(root)
    for j in range(3):
        button=Button(buttonFrame,text=str(list2[increament]),font="lucida 25 bold",bg="grey",width=4)
        if j==2:
            button.pack(side=LEFT,ipadx=49,ipady=1)
        else:
            button.pack(side=LEFT,ipadx=2,ipady=1) 
        button.bind("<Button-1>",click)
        increament+=1
    buttonFrame.pack()         

root.mainloop()