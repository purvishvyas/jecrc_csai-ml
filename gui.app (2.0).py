# GUI - Graphical User Interface

#Libraries
# #############
# 1. Tkinter
# 2. pyQT
# 3. Turtle


import tkinter as ttk

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

ttk.Entry(app, textvariable=f1 , font = ('Arial', 22)).place(x= 50, y = 200)
ttk.Entry(app , textvariable=f2, font = ('Arial', 22)).place(X=150,Y=200)
def calci():
    print('I will calculate')
    ttk.Button(app, text='+', command = calci ,font = ('Arial',22)).place(x= 50, y = 240)
    ttk.Button(app, text='-', command = calci ,font = ('Arial',22)).place(x= 100, y = 240)
    ttk.Button(app, text='*', command = calci ,font = ('Arial',22)).place(x= 150, y = 240)
    ttk.Button(app, text='/', command = calci ,font = ('Arial',22)).place(x= 200, y = 240)


app.mainloop()