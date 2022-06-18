#Adityaᵀᴹ

from tkinter import *
from pyautogui import typewrite,press
from time import sleep


root=Tk()
root.geometry('400x200')

class encryptor:
    @staticmethod
    def encrypt():
        global s1
        l2.grid_remove()
        a=str(e1.get()).upper()
        a.strip()

        b=''
        for i in a:
            if i.isalpha():
                b+=str(ord(i)-64)+','
            elif i==' ':
                b+=' ; ,'
            else:
                b+=i
        s1=b    
        l2.config(text=b)
        l2.grid(row=1,column=0,padx=10,pady=10,columnspan=3)

    @staticmethod
    def Encryptor_grid():
        l3.grid_remove()
        e2.grid_remove()
        b4.grid_remove()
        b5.grid_remove()
        b6.grid_remove()
        extra.clear()

        l1.grid(row=0,column=0,padx=10,pady=10)
        e1.grid(row=0,column=1,padx=10,pady=10)
        b1.grid(row=2,column=0,padx=10,pady=10)
        b2.grid(row=2,column=1,padx=10,pady=10)
        b3.grid(row=2,column=2,padx=10,pady=10)

class decoder:
    @staticmethod
    def Decoder():
        global s1
        a=str(e2.get())
        l4.grid_remove()
        b=''
        l=a.split(',')
        for i in l:
            if i.isdigit():
                c=int(i)+64
                b+=chr(c)
            elif i==" ; ":
                b+=" "
            else:
                b+=i
        b=b.title()
        s1=b
        l4.config(text=b)
        l4.grid(row=1,column=0,padx=10,pady=10,columnspan=3)      

    @staticmethod
    def Decoder_grid():
        l1.grid_remove()
        e1.grid_remove()
        b1.grid_remove()
        b2.grid_remove()
        b3.grid_remove()
        extra.clear()
        l3.grid(row=0,column=0,padx=10,pady=10)
        e2.grid(row=0,column=1,padx=10,pady=10)
        b4.grid(row=2,column=0,padx=10,pady=10)
        b5.grid(row=2,column=1,padx=10,pady=10)
        b6.grid(row=2,column=2,padx=10,pady=10)

class extra:
    @staticmethod
    def clear():
        l2.grid_remove()
        l4.grid_remove()
        e1.delete(0,END)
        e2.delete(0,END)

    @staticmethod
    def paste():
        sleep(3)
        typewrite(s1)
        press('Enter')




#Menu

M=Menu(root)
root.config(menu=M)

m1=Menu(M)
M.add_cascade(label='Select', menu=m1)
m1.add_command(label='Encrypter',command=encryptor.Encryptor_grid)
m1.add_separator()
m1.add_command(label='Decoder',command=decoder.Decoder_grid)



#Encryptor
l1=Label(text='Input',padx=3,pady=2)
l2=Label(text='',padx=3,pady=2,borderwidth=2,relief='solid')
e1=Entry()
b1=Button(text='Encrypt',padx=3,pady=2,command=encryptor.encrypt)
b2=Button(text='Clear',padx=3,pady=2,command=extra.clear)
b3=Button(text='Paste',padx=3,pady=2,command=extra.paste)

#Decoder
l3=Label(text='Input',padx=3,pady=2)
l4=Label(text='',padx=3,pady=2,borderwidth=2,relief='solid')
e2=Entry()
b4=Button(text='Decode',padx=3,pady=2,command=decoder.Decoder)
b5=Button(text='Clear',padx=3,pady=2,command=extra.clear)
b6=Button(text='Paste',padx=3,pady=2,command=extra.paste)

encryptor.Encryptor_grid()




root.mainloop()
