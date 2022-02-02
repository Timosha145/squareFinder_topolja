from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np

def handler():    
    if (a.get()!="" and b.get()!="" and c.get()!=""):
        a1=int(a.get())
        b1=int(b.get())
        c1=int(c.get())
        D=b1*b1-4*a1*c1
        if D>0:
            xround=round((-1*b1+sqrt(D))/(2*a1),2)
            xround1=round((-1*b1-sqrt(D))/(2*a1),2)
            t=f"X1={xround} \nX2={xround1}"
            flag=True
        elif D==0:
            xround=round((-1*b1)/(2*a1),2)
            t=f"X1={xround}"
            flag=True
        else:
            t="Корней нет"
            flag=False
        lblResult.configure(text=f"D={D}\n{t}")
    return flag,D,t
def graafik():
    flag,D,t=handler()
    if flag==True:
        a1=int(a.get())
        b1=int(b.get())
        c1=int(c.get())
        x0=(-b1)/(2*a1)
        y0=a1*x0*x0+b1*x0+c1
        x = np.arange(x0-10, x0+10, 0.5)
        y=a1*x*x+b1*x+c1
        fig = plt.figure()
        plt.plot(x, y,'b:o', x0, y0,'g-d')
        plt.title('Квадратное уравнение')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
        text=f"Вершина параболлы ({x0},{y0})"
    else:
        text=f"График нет возможности построить"
    lblResult.configure(text=f"D={D}\n{t}\n{text}")
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

button1=Button(window,text="График",font="Arial 20",width=8,bg="green",command=graafik)
button1.pack(side=LEFT)

window.mainloop()
