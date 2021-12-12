# BasicGUI.py

from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.geometry('500x400')
GUI.title('โปรแกรมของลุง')


file = PhotoImage(file='durian.png')
IMG = Label(GUI,image=file,text='')
IMG.pack()

L1 = Label(GUI,text='โปรแกรมคำนวณทุเรียน',font=('Angsana New',30,'bold'))
L1.pack()# .place(x,y) , .grid(row=0,column=0)

L2 = Label(GUI,text='กรุณากรอกจำนวนทุเรียน',font=('Angsana New',20))
L2.pack

v_quantity = StringVar()

E1 = Entry(GUI,textvariable=v_quantity)
E1.pack()

def Calculate():
	quantity = v_quantity.get()
	price = 100
	print('จำนวน',float(quantity) * price)
	cal = float(quantity) * price
	messagebox.showinfo('ยอดที่ลูกค้าต้องจ่าย','ทุเรียนจำนวน {} กิโลกรัม ราคาทั้งหมด: {:,.2f} บาท'.format(quantity,cal))


B1 = ttk.Button(GUI, text = 'คำนวณ',command=Calculate)
B1.pack(ipadx=30,ipady=20,pady=20)

GUI.mainloop()