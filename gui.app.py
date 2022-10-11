# GUI - Graphical User Interface

#Libraries
# #############
# 1. Tkinter
# 2. pyQT
# 3. Turtle


import tkinter as ttk
from unittest import result

app = ttk.Tk()
app.title('My App')
app.geometry('600x400')
msg = ttk.Variable(app)
print(msg.get())
msg.set('Empty')
print(msg.get())
ttk.Label(app, text = 'A simple Text Label').place(x = 50 , y = 50)
ttk.Label(app , textvariable=msg).place(x =100 , y = 70)



ttk.Label(app, text='heloo').place(x=20,y=30)
def abc():
    print('Wow')
    msg.set('Jo tera mann kare')
ttk.Button(app , text = 'Isko Click Karo',font = ('Arial',25), command = abc).place(x = 100 , y =100)
ttk.Button(app , text = 'Ye wala bhi hai', font = ('Arial', 25), command =lambda:msg.set('Pata nhi')).place(x =100 , y = 150)

f1= ttk.Variable(app)
f1.set('0')
f2 = ttk.Variable(app)
f2.set('0')
result = ttk.Variable(app)

ttk.Entry(app, textvariable=f1 , font = ('Arial', 22)).place(x= 50, y = 200)
ttk.Entry(app , textvariable=f2, font = ('Arial', 22)).place(x=150,y=200)
ttk.Label(app, text = 'Result').place(x=100,y=300)
ttk.Label(app,textvariable=result, font=('Arial',22)).place(x=100,y=330)
def calci(op):
    print('I will calculate')
    result.set(eval(f1.get()+op+f2.get()))
ttk.Button(app, text='+', command = lambda:calci('+') ,font = ('Arial',22)).place(x= 50, y = 240)
ttk.Button(app, text='-', command = lambda:calci('-') ,font = ('Arial',22)).place(x= 150, y = 240)
ttk.Button(app, text='*', command = lambda:calci('*'),font = ('Arial',22)).place(x= 250, y = 240)
ttk.Button(app, text='/', command = lambda:calci('/') ,font = ('Arial',22)).place(x= 350, y = 240)

box = ttk.Listbox(app, height=5,fg='blue',activestyle='dotbox')
box.insert(1,'Sample1')
box.insert(2,'Sample2')
box.insert(3,'Sample3')

box.place(x=350,y=40)

def show():
    print(box.get(box.curselection()))

ttk.Button(app,text='show',command=show).place(x=350,y=250)

app.mainloop()