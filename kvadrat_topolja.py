from tkinter import *
from math import *

def squareFinder(event):
	a.config(bg="cyan")
	b.config(bg="cyan")
	c.config(bg="cyan")
	isOK=0
	try:
		aNum=float(a.get())
	except ValueError:
		a.config(bg="red")
		isOK=1
	try:
		bNum=float(b.get())
	except ValueError:
		b.config(bg="red")
		isOK=1
	try:
		cNum=float(c.get())
	except ValueError:
		c.config(bg="red")
		isOK=1
	if isOK==0:
		D=bNum**2-4*aNum*cNum
		if D>0:
			x1=(-1*bNum+sqrt(D))/2*aNum
			x2=(bNum+sqrt(D))/2*aNum
			lblResult.config(text=f"D={D}\n x1={round(x1,2)}\n x2={round(x2,2)}")
		elif D==0:
			x1=-1*bNum/2*aNum
			lblResult.config(text=f"D={D}\n x={round(x1,2)}")
		else:
			lblResult.config(text=f"D={D}\n корней нет")

window=Tk()
window.title("Квадратное уравнение")
window.geometry("600x300")

lbl=Label(window,text="Решение квадратного уравнения",font="Arial 25",height=2,width=35,bg="cyan")
lbl.pack()
lblResult=Label(window,text="",font="Arial 20",height=3,width=20,bg="cyan")
lblResult.pack(side=BOTTOM)

a=Entry(window,bg="cyan",font="Arial 20",width=3,justify=LEFT)
a.pack(side=LEFT)
a.bind("<Return>",squareFinder)

lbl=Label(window,text="x**2 +",font="Arial 20",height=1,width=5)
lbl.pack(side=LEFT)
()
b=Entry(window,bg="cyan",font="Arial 20",width=3,justify=LEFT)
b.pack(side=LEFT)
b.bind("<Return>",squareFinder)

lbl=Label(window,text="x+",font="Arial 20",height=1,width=2)
lbl.pack(side=LEFT)

c=Entry(window,bg="cyan",font="Arial 20",width=3,justify=LEFT)
c.pack(side=LEFT)
c.bind("<Return>",squareFinder)

lbl=Label(window,text="=0",font="Arial 20",height=1,width=2)
lbl.pack(side=LEFT)

buttonSolve=Button(window,text="Решить",font="Arial 20",width=8,bg="green")
buttonSolve.pack(side=LEFT)
buttonSolve.bind("<Button-1>",squareFinder)

button1=Button(window,text="График",font="Arial 20",width=8,bg="green")
button1.pack(side=LEFT)

window.mainloop()