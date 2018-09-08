#-*-coding: utf-8-*-

#PyCalc
#Made By: Amin Karic

from tkinter import *
import math

class PyCalc:
    
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

 def cube(self):
   self.getandreplace()
   try: 
    self.value= eval(self.newtext) 
   except (SyntaxError, NameError, ZeroDivisionError):
    self.e.delete(0,END)
    self.e.insert(0,'Invalid Syntax!')
   else:
    self.cube=math.pow(self.value, 3)
    self.e.delete(0,END)
    self.e.insert(0,self.cube)

 def pi(self):
   self.getandreplace()
   try: 
    self.value= '3.14159265359'
   except  (SyntaxError, NameError, ZeroDivisionError):
    self.e.delete(0,END)
    self.e.insert(0,'Invalid Syntax!')
   else:
    self.e.insert(END, self.value)

    
 def abs(self):
   self.getandreplace()
   try: 
    self.value= eval(self.newtext) 
   except (SyntaxError, NameError, ZeroDivisionError):
    self.e.delete(0,END)
    self.e.insert(0,'Invalid Syntax!')
   else:
    if self.value < 0 :
     self.e.delete(0,END)
     self.e.insert(0, self.value)
     self.e.delete(0,1)
    else:
       self.e.delete(0, END)
       self.e.insert(0, self.value)

 def cos(self):
   self.getandreplace()
   try: 
    self.value= eval(self.newtext) 
   except (SyntaxError, NameError, ZeroDivisionError):
     self.e.delete(0,END)
     self.e.insert(0,'Invalid Syntax!')
   else:
     self.cos = math.cos(self.value)
     self.e.delete(0,END)
     self.e.insert(0, self.cos)

 def sin(self):
   self.getandreplace()
   try: 
    self.value= eval(self.newtext) 
   except (SyntaxError, NameError, ZeroDivisionError):
     self.e.delete(0,END)
     self.e.insert(0,'Invalid Syntax!')
   else:
     self.sin = math.sin(self.value)
     self.e.delete(0,END)
     self.e.insert(0, self.sin)

 def tan(self):
   self.getandreplace()
   try: 
    self.value= eval(self.newtext)
   except (SyntaxError, NameError, ZeroDivisionError):
     self.e.delete(0,END)
     self.e.insert(0,'Invalid Syntax!')
   else:
     self.tan = math.tan(self.value)
     self.e.delete(0,END)
     self.e.insert(0,  self.tan)

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
root = Tk()
obj=PyCalc(root) 
root.configure(background="lightblue")
root.wm_iconbitmap("Calc3.ico")
root.mainloop()
