import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from math import sin,cos,tan
from tkinter import *

#creating GUI
m = tk.Tk()
m.geometry('320x400')
m.title('Graphical calculator')

lbl = Label(m,text = "Use ** for putting power  \n********************** ")
lbl.grid(column=1,row=0)

lbl = Label(m,text = " ")
lbl.grid(column=1,row=1)

lbl = Label(m,text = " ")
lbl.grid(column=1,row=2)

#complete workspace 
lbl = Label(m,text = "Enter the equation below")
lbl.grid(column=1,row=3)

text = Entry(m,width=10)
text.grid(column=1,row=4)

lbl2 = Label(m,text = " \n")
lbl2.grid(column=1,row=8)

lbl2 = Label(m,text = "Enter point to get value")
lbl2.grid(column=1,row=9)

lbl3 = Label(m,text = "initial point")
lbl3.grid(column=0,row=6)

lbl4 = Label(m,text = "end point")
lbl4.grid(column=2,row=6)

text2 = Entry(m,width=10)
text2.grid(column=1,row=10)

text3 = Entry(m,width=5)
text3.grid(column=2,row=7)

text4 = Entry(m,width=5)
text4.grid(column=0,row=7)


def clicked():
	function1= text.get()

	#function for converting string to function
	def f1(x):
		for i in range(0,len(function1)):
			if(function1[i]=='s'or function1[i]=='c' or function1[i]=='t'):
				function1[:i-1]+"np."+function1[i:]
				break
		return eval(function1)

	# intial value of the plot
	inti= text3.get()
	#final value of the plot
	fin= text4.get()
	
	#converting string to integer
	def str_to_int(string):
		if(len(string)==2):
			return int(string,base=10)
		return int(string)

	#points on x axis 
	xlist1 = np.linspace(str_to_int(inti),str_to_int(fin),num=10000)
	#point on y axis	
	ylist1= []
	for i in range(0,10000):
		ylist1.append(f1(xlist1[i]))

	plt.plot(xlist1,ylist1)
	
	#Plotting some point of value if required
	function2= text2.get()
	x=[]
	def con(string):
		li = list(string.split(" "))
		return li
	list2 = con(function2)

	#conveting given point in ineger form
	for i in range(0,np.size(list2)):
		if(list2[i]==' '):
			continue
		if(len(list2[i])==2):
			ans = (list2[i][0]) + (list2[i][1])
			x.append(int(ans,base=10))
			continue
		if(len(list2[i])==1):
			x.append(int(list2[i]))
	y=[]

	for i in range(0,np.size(x)):
		y.append(f1(x[i]))

	#printing value at given point
	lbl5 = Label(m,text = f"{y}")
	lbl5.grid(column=1,row=11)
	
	#ploting the points
	plt.scatter(x,y)
	plt.grid()	
	plt.show()
		
# button widget with red color text inside
btn = Button(m, text = "solve" ,
             fg = "red", command=clicked)
# Set Button Grid
btn.grid(column=1, row=5)
m.mainloop()


