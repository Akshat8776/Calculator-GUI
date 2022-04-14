import math
from tkinter import *
window=Tk()
window.title("Calculator")
window.config(padx=50,pady=50)
window.minsize(width=250,height=500)
window.configure(bg="white")

def clearcon():
    entry1.delete(0,"end")
    entry1.insert(END,string="")
    entry2.delete(0,"end")
    entry2.insert(END,string="")
    ans.config(text="")

def nextcalc():
    if ans["text"]!="":
        entry1.delete(0,"end")
        entry1.insert(END,string=ans["text"])
        entry2.delete(0,"end")
        entry2.insert(END,string="")
        ans.config(text="")
    
def add():
    num1=float(entry1.get())
    num2=float(entry2.get())
    sum=num1+num2
    st=str(sum)
    ans.config(text=st)
    
def sub():
    num1=float(entry1.get())
    num2=float(entry2.get())
    sub=num1-num2
    st=str(sub)
    ans.config(text=st)
    
def mult():
    num1=float(entry1.get())
    num2=float(entry2.get())
    mul=num1*num2
    st=str(mul)
    ans.config(text=st)

def div():
    num1=float(entry1.get())
    num2=float(entry2.get())
    if num2!=0:
        divd=num1/num2
        st=str(divd)
        ans.config(text=st)
    
def mode():
    num1=int(entry1.get())
    num2=int(entry2.get())
    md=num1%num2
    st=str(md)
    ans.config(text=st)
    
def loga():
    num1=float(entry1.get())
    n=entry2.get()
    if n=="":
        sub=math.log10(num1)
    else:
        num2=float(n)
        sub=math.log(num1,num2)
    st=str(sub)
    ans.config(text=st)
  
def pow():
    num1=float(entry1.get())
    num2=float(entry2.get())
    pw=math.pow(num1,num2)
    st=str(pw)
    ans.config(text=st)

def rt():
    num1=float(entry1.get())
    num2=float(entry2.get())
    pw=math.pow(num1,1/num2)
    st=str(pw)
    ans.config(text=st)

def permu():
    num1=int(entry1.get())
    num2=int(entry2.get())
    res=math.factorial(num1)/math.factorial(num2)
    st=str(res)
    ans.config(text=st)

def combi():
    num1=int(entry1.get())
    num2=int(entry2.get())
    res=math.factorial(num1)/(math.factorial(num2)*math.factorial(num1-num2))
    st=str(res)
    ans.config(text=st)
   
def pi():
    entry1.delete(0,"end")
    entry1.insert(END,string=str(math.pi))
    
def exp():
    entry1.delete(0,"end")
    s=math.e
    entry1.insert(END,string=str(s))

def fact():
    num1=int(entry1.get())
    res=math.factorial(num1)
    st=str(res)
    ans.config(text=st)

def sin():
    num1=float(entry1.get())
    res=math.sin(math.radians(num1))
    st=str(res)
    ans.config(text=st)

def cos():
    num1=float(entry1.get())
    res=math.cos(math.radians(num1))
    st=str(res)
    ans.config(text=st)
    
def tan():
    num1=float(entry1.get())
    res=math.tan(math.radians(num1))
    st=str(res)
    ans.config(text=st)
    
def sininv():
    num1=float(entry1.get())
    res=math.degrees(math.asin(num1))
    st=str(res)
    ans.config(text=st)  
    
def cosinv():
    num1=float(entry1.get())
    res=math.degrees(math.acos(num1))
    st=str(res)
    ans.config(text=st)
    
def taninv():
    num1=float(entry1.get())
    res=math.degrees(math.atan(num1))
    st=str(res)
    ans.config(text=st)

def sqrt():
    num1=float(entry1.get())
    res=math.sqrt(num1)
    st=str(res)
    ans.config(text=st)


#entries
entry1=Entry(width=20)
entry1.insert(END,string="0")
entry1.configure(background="white")
entry1.focus()
entry1.grid(column=4,row=0)

entry2=Entry(width=20)
entry2.insert(END,string="0")
entry2.configure(background="white")
entry2.grid(column=4,row=1)

#label
ans=Label(text="   ")
ans.grid(column=4,row=2)
ans.configure(background="white")

text1=Label(text="Enter num 1 : ")
text1.grid(column=0,row=0)
text1.configure(background="white")

text2=Label(text="Enter num 2 : ")
text2.grid(column=0,row=1)
text2.configure(background="white")

text3=Label(text="Answer  : ")
text3.grid(column=0,row=2)
text3.configure(background="white")

#buttons
butcle=Button(text="C",command=clearcon)
butcle.config(width=5,height=3)
butcle.place(x=94,y=70)

butnext=Button(text="N",command=nextcalc)
butnext.config(width=5,height=3)
butnext.place(x=141,y=70)

butsum=Button(text="+",command=add)
butsum.config(width=5,height=3)
butsum.place(x=0,y=130)

butsub=Button(text="-",command=sub)
butsub.config(width=5,height=3)
butsub.place(x=47,y=130)

butmul=Button(text="*",command=mult)
butmul.config(width=5,height=3)
butmul.place(x=94,y=130)

butdiv=Button(text="/",command=div)
butdiv.config(width=5,height=3)
butdiv.place(x=141,y=130)

butmd=Button(text="%",command=mode)
butmd.config(width=5,height=3)
butmd.place(x=0,y=190)

butpow=Button(text="pow",command=pow)
butpow.config(width=5,height=3)
butpow.place(x=47,y=190)

butsqrt=Button(text="sqrt",command=sqrt)
butsqrt.config(width=5,height=3)
butsqrt.place(x=94,y=190)

butrt=Button(text="root",command=rt)
butrt.config(width=5,height=3)
butrt.place(x=141,y=190)

butlg=Button(text="log",command=loga)
butlg.config(width=5,height=3)
butlg.place(x=0,y=250)

butsin=Button(text="sin",command=sin)
butsin.config(width=5,height=3)
butsin.place(x=47,y=250)

butcos=Button(text="cos",command=cos)
butcos.config(width=5,height=3)
butcos.place(x=94,y=250)

buttan=Button(text="tan",command=tan)
buttan.config(width=5,height=3)
buttan.place(x=141,y=250)

butpi=Button(text="pi",command=pi)
butpi.config(width=5,height=3)
butpi.place(x=0,y=310)

butsini=Button(text="sininv",command=sininv)
butsini.config(width=5,height=3)
butsini.place(x=47,y=310)

butcosi=Button(text="cosinv",command=cosinv)
butcosi.config(width=5,height=3)
butcosi.place(x=94,y=310)

buttani=Button(text="taninv",command=taninv)
buttani.config(width=5,height=3)
buttani.place(x=141,y=310)

butp=Button(text="nPr",command=permu)
butp.config(width=5,height=3)
butp.place(x=0,y=370)

butc=Button(text="nCr",command=combi)
butc.config(width=5,height=3)
butc.place(x=47,y=370)

bute=Button(text="e",command=exp)
bute.config(width=5,height=3)
bute.place(x=94,y=370)

butfact=Button(text="!",command=fact)
butfact.config(width=5,height=3)
butfact.place(x=141,y=370)

window.mainloop()