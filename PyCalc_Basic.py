﻿#-*-coding: utf-8-*-

#PyCalc V2.0
#Made By: Amin Karic

from tkinter import *
from tkinter.colorchooser import askcolor
import math
import os
import pathlib

root = Tk()
try:
  root.wm_iconbitmap(os.path.join(pathlib.Path(__file__).parent.absolute(), "Calc3.ico"))
except:
  pass

class PyCalc:

 def BgCol(self):
    bg_col = askcolor()
    bg_c_ol = bg_col[1]
    root.configure(bg=bg_c_ol)


 def getandreplace(self):
  self.expression = self.e.get()
  self.newtext=self.expression.replace(self.div,'/')
  self.newtext=self.newtext.replace('x','*')

 def equals(self):
  self.getandreplace()
  try: 
   self.value= eval(self.newtext)
  except (SyntaxError, NameError, ZeroDivisionError):
   self.e.delete(0,END)
   self.e.insert(0,'Invalid Syntax!')
  else:
   self.e.delete(0,END)
   self.e.insert(0,self.value)
 
 def squareroot(self):
  self.getandreplace()
  try: 
   self.value= eval(self.newtext) 
  except(SyntaxError, NameError, ZeroDivisionError):
   self.e.delete(0,END)
   self.e.insert(0,'Invalid Syntax!')
  else:
   self.sqrtval=math.sqrt(self.value)
   self.e.delete(0,END)
   self.e.insert(0,self.sqrtval)

 def square(self):
  self.getandreplace()
  try: 
   self.value= eval(self.newtext) 
  except (SyntaxError, NameError, ZeroDivisionError):
   self.e.delete(0,END)
   self.e.insert(0,'Invalid Syntax!')
  else:
   self.sqval=math.pow(self.value,2)
   self.e.delete(0,END)
   self.e.insert(0,self.sqval)

 def clearall(self): 
  self.e.delete(0,END)
 
 def clear1(self):
  self.txt=self.e.get()[:-1]
  self.e.delete(0,END)
  self.e.insert(0,self.txt)

 def action(self,argi): 
  self.e.insert(END,argi)
 
 def __init__(self,master):
  master.title('PyCalc Basic')
  master.geometry()
  self.e = Entry(master)
  self.e.grid(row=0,column=0,columnspan=8,pady=5)
  self.e.focus_set()


  self.div='/'

#Button Generate
  Button(master,text="=",width=11, bg="red", fg="white", command=lambda:self.equals()).grid(row=4, column=4,columnspan=2)
  Button(master,text='AC',width=4, bg="orange", fg="white", command=lambda:self.clearall()).grid(row=1, column=4)
  Button(master,text='C',width=4, bg="orange", fg="white", command=lambda:self.clear1()).grid(row=1, column=5)
  Button(master,text="+", bg="grey", fg="white", width=4,command=lambda:self.action('+')).grid(row=4, column=3)
  Button(master,text="x",width=4, bg = "grey", fg="white", command=lambda:self.action('x')).grid(row=2, column=3)
  Button(master,text="-",width=4, bg="grey", fg="white", command=lambda:self.action('-')).grid(row=3, column=3)
  Button(master,text="÷",width=4, bg ="grey", fg="white", command=lambda:self.action(self.div)).grid(row=1, column=3) 
  Button(master,text="%",width=4, bg="grey", fg="white", command=lambda:self.action('%')).grid(row=4, column=2)
  Button(master,text="7",width=4,command=lambda:self.action(7)).grid(row=1, column=0)
  Button(master,text="8",width=4,command=lambda:self.action(8)).grid(row=1, column=1)
  Button(master,text="9",width=4,command=lambda:self.action(9)).grid(row=1, column=2)
  Button(master,text="4",width=4,command=lambda:self.action(4)).grid(row=2, column=0)
  Button(master,text="5",width=4,command=lambda:self.action(5)).grid(row=2, column=1)
  Button(master,text="6",width=4,command=lambda:self.action(6)).grid(row=2, column=2)
  Button(master,text="1",width=4,command=lambda:self.action(1)).grid(row=3, column=0)
  Button(master,text="2",width=4,command=lambda:self.action(2)).grid(row=3, column=1)
  Button(master,text="3",width=4,command=lambda:self.action(3)).grid(row=3, column=2)
  Button(master,text="0",width=4,command=lambda:self.action(0)).grid(row=4, column=0)
  Button(master,text=".", width=4, bg="grey", fg="white", command=lambda:self.action('.')).grid(row=4, column=1)
  Button(master,text="(",width=4,  bg="grey", fg="white", command=lambda:self.action('(')).grid(row=2, column=4)
  Button(master,text=")",width=4,  bg="grey", fg="white", command=lambda:self.action(')')).grid(row=2, column=5)
  Button(master,text="√",width=4,  bg="grey", fg="white", command=lambda:self.squareroot()).grid(row=3, column=4)
  Button(master,text="x²",width=4,  bg="grey", fg="white",command=lambda:self.square()).grid(row=3, column=5)
  Button(master,text="Set Background Color",width=34,  bg="black", fg="white",command=lambda:self.BgCol()).grid(row=5, column=0, columnspan=6)
obj=PyCalc(root) 
root.mainloop()
