#-*- coding: utf-8 -*-
from tkinter import *
raiz=Tk()
raiz.config(bg="blue")
frame=Frame(raiz)
frame.config(bg="red")
frame.pack()

resultado=str()


escribir1=Entry(frame, font=("Helvetica", 32), justify='right')
escribir1.config(width="15")
escribir1.grid(row="0",column="0",columnspan="3")

escribir2=Entry(frame, font=("Helvetica", 32),justify='right')
escribir2.config(width="5")
escribir2.grid(row="0",column="3")


def f(num):
	global resultado
	resultado=resultado+num
	print(resultado)
	escribir1.delete(0,len(resultado))
	escribir1.insert(0,resultado)
def igual():
	global resultado
	a=escribir1.get()
	a=a.replace("-","+-")
	print("voy a analizar esta cadena: ",a)
	split1=a.split("+")
	r=-1
	resultadototal=0
	for s in split1:
		r+=1
		if ("x" in s):
			solucionmultiplicacion=1
			m=s.split("x")
			for s2 in m:
				solucionmultiplicacion*=int(s2)
			split1[r]=solucionmultiplicacion
			print("he solucionado una multiplicación",solucionmultiplicacion)
	resultadototal=0
	for s in split1:
		if s=='':
			s="0"
		resultadototal+=int(s)
		print("he sumado ",resultadototal)
	escribir2.delete(0,len(str(resultadototal)))
	escribir2.insert(0,resultadototal)
	escribir1.delete(0,len(resultado))
	escribir1.insert(0,resultadototal)
	resultado=str(resultadototal)
	print("resultado: ",resultado)
	print("resultadototal: ",resultadototal)
def borrar():
	global resultado
	escribir1.delete(len(escribir1.get())-1,len(escribir1.get()))
	resultado=escribir1.get()
	print("he borrado y se ha quedado así: ",resultado)
	escribir1.delete(0,len(resultado))
	escribir1.insert(0,resultado)
#---------------------------------------------#	

boton1=Button(frame, text="1", font=("Helvetica", 32), command=lambda: f("1"))
boton1.config(width="5",height="2")
boton1.grid(row=1, column="0")

boton2=Button(frame, text="2", font=("Helvetica", 32), command=lambda: f("2"))
boton2.config(width="5",height="2")
boton2.grid(row=1, column="1")

boton3=Button(frame, text="3", font=("Helvetica", 32), command=lambda: f("3"))
boton3.config(width="5",height="2")
boton3.grid(row=1, column="2")

boton4=Button(frame, text="4", font=("Helvetica", 32), command=lambda: f("4"))
boton4.config(width="5",height="2")
boton4.grid(row=2, column="0")

boton5=Button(frame, text="5", font=("Helvetica", 32), command=lambda: f("5"))
boton5.config(width="5",height="2")
boton5.grid(row=2, column="1")

boton6=Button(frame, text="6", font=("Helvetica", 32), command=lambda: f("6"))
boton6.config(width="5",height="2")
boton6.grid(row=2, column="2")

boton7=Button(frame, text="7", font=("Helvetica", 32), command=lambda: f("7"))
boton7.config(width="5",height="2")
boton7.grid(row=3, column="0")

boton8=Button(frame, text="8", font=("Helvetica", 32), command=lambda: f("8"))
boton8.config(width="5",height="2")
boton8.grid(row=3, column="1")

boton9=Button(frame, text="9", font=("Helvetica", 32), command=lambda: f("9"))
boton9.config(width="5",height="2")
boton9.grid(row=3, column="2")

boton0=Button(frame, text="0", font=("Helvetica", 32), command=lambda: f("0"))
boton0.config(width="5",height="2")
boton0.grid(row=4, column="0")

boton000=Button(frame, text="000", font=("Helvetica", 32), command=lambda: f("000"))
boton000.config(width="5",height="2")
boton000.grid(row=4, column="1")

suma=Button(frame, text="+",command=lambda: f("+"), font=("Helvetica", 32))
suma.config(width="5",height="2")
suma.grid(row=1, column="3")

resta=Button(frame, text="-",command=lambda: f("-"), font=("Helvetica", 32))
resta.config(width="5",height="2")
resta.grid(row=2, column="3")

multiplicacion=Button(frame, text="x", command=lambda: f("x"), font=("Helvetica", 32))
multiplicacion.config(width="5",height="2")
multiplicacion.grid(row=3, column="3")

igual=Button(frame, text="=",command=igual, font=("Helvetica", 32))
igual.config(width="5",height="2")
igual.grid(row="4", column="3")

borrar=Button(frame, text="␡",command=borrar, font=("Helvetica", 32))
borrar.config(width="5",height="2")
borrar.grid(row="4", column="2")



raiz.mainloop()
