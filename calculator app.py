from tkinter import*

window=Tk()
window.title("calculator app")

myentry=Entry(window,width=50,borderwidth=5,bg="sky blue")
myentry.grid(row=0,column=0,columnspan=3)


def buttonclick(number):
    currentnum=myentry.get()
    myentry.delete(0,END)
    myentry.insert(0,str(currentnum)+str(number))
    

def clear():
    myentry.delete(0,END)


def button_add():
    firstnum=myentry.get()
    global f_num
    f_num=int(firstnum)
    myentry.delete(0,END)
    global math
    math="+"


def button_subtract():
     firstnum=myentry.get()
     global f_num
     global math
     f_num=int(firstnum)
     myentry.delete(0,END)
     math="-"    

def button_multiply():
     firstnum=myentry.get()
     global f_num
     global math
     f_num=int(firstnum)
     myentry.delete(0,END)
     math="*"


def button_divide():
     firstnum=myentry.get()
     global f_num
     global math
     f_num=int(firstnum)
     myentry.delete(0,END)
     math="/"



def button_equal():
    global f_num
    global math
    secondnum=myentry.get()
    
    global s_num
    s_num=int(secondnum)
    myentry.delete(0,END)
    
    if math == "+":    
        myentry.insert(0,f_num + s_num)

    if math == "-":
        myentry.insert(0,f_num - s_num)


    if math == "*":
        myentry.insert(0,f_num * s_num)

    if math == "/":
        myentry.insert(0,f_num / s_num )    





button1=Button(window,padx=40,pady=20,text="1",command=lambda:buttonclick(1))
button2=Button(window,padx=40,pady=20,text="2",command=lambda:buttonclick(2))
button3=Button(window,padx=40,pady=20,text="3",command=lambda:buttonclick(3))

button4=Button(window,padx=40,pady=20,text="4",command=lambda:buttonclick(4))
button5=Button(window,padx=40,pady=20,text="5",command=lambda:buttonclick(5))
button6=Button(window,padx=40,pady=20,text="6",command=lambda:buttonclick(6))

button7=Button(window,padx=40,pady=20,text="7",command=lambda:buttonclick(7))
button8=Button(window,padx=40,pady=20,text="8",command=lambda:buttonclick(8))
    
button9=Button(window,padx=40,pady=20,text="9",command=lambda:buttonclick(9))
button0=Button(window,padx=40,pady=20,text="0",command=lambda:buttonclick(0))


buttonclear=Button(window,text="clear",padx=32,pady=20,command=clear)
buttonadd=Button(window,text="+",padx=34,pady=25,command=button_add)
buttonequal=Button(window,text="=",padx=30,pady=25,command=button_equal)

buttonmultiply=Button(window,text='X',padx=40,pady=20,command=button_multiply)
buttondivide=Button(window,text="/",padx=40,pady=20,command=button_divide)
buttonsubtract=Button(window,text="-",padx=40,pady=20,command=button_subtract)
buttonexit=Button(window,text="exit",padx=32,pady=20,command=window.quit)


button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
buttonclear.grid(row=6,column=1)
buttonadd.grid(row=4,column=2)

buttonequal.grid(row=5,column=2)
buttonmultiply.grid(row=5,column=0)
buttondivide.grid(row=5,column=1)

buttonsubtract.grid(row=4,column=1)
buttonexit.grid(row=6,column=2)
window.mainloop()