# BasicGUI.py

from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
#######################
def timestamp(thai=True):
	if thai == True:
		stamp = datetime.now()
		stamp = stamp.replace(year=stamp.year+543) # บวกปีเป็น พ.ศ.
		stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	else: 
		stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	return stamp

def writecsv(data):
	# data = ['Time','10', 500]
	with open('data.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file) # fw = file writer
		fw.writerow(data)
	print('Success')

def writecsv(data):
	# data = ['Time','10', 500]
	with open('data.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file) # fw = file writer
		fw.writerow(data)


GUI = Tk()
GUI.geometry('500x400')
GUI.title('โปรแกรมคำนวณบิตคอยน์')


file = PhotoImage(file='bitcoin.png')
IMG = Label(GUI,image=file,text='')
IMG.pack()

L1 = Label(GUI,text='โปรแกรมคำนวณบิตคอยน์',font=('Angsana New',30,'bold'))
L1.pack()# .place(x,y) , .grid(row=0,column=0)

L2 = Label(GUI,text='กรุณากรอกจำนวนบิตคอยน์',font=('Angsana New',30))
L2.pack

v_quantity = StringVar()

E1 = Entry(GUI,textvariable=v_quantity)
E1.pack()

def Calculate():
	quantity = v_quantity.get()
	price = 2000000
	print('จำนวน',float(quantity) * price)
	cal = float(quantity) * price

	# EN Date
	stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	# THAI DATE
	stamp = datetime.now()
	stamp = stamp.replace(year=stamp.year+543) # บวกปีเป็น พ.ศ.
	stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')

	# ฟังชั่นบันทึกข้อมูลไฟล์ txt
	filename = 'data.txt'
	with open(filename,'a',encoding='utf-8') as file:
		file.write('\n' + 'วัน-เวลา: {} บิตคอยน์: {} เหรียญ ราคาทั้งหมด: {:,.2f} บาท'.format(stamp,quantity,cal))


	#


	# pop up
	messagebox.showinfo('ยอดที่ลูกค้าต้องจ่าย','บิตคอยน์จำนวน {} เหรียญ ราคาทั้งหมด: {:,.2f} บาท'.format(quantity,cal))



B1 = ttk.Button(GUI, text = 'Calculate',command=Calculate)
B1.pack(ipadx=50,ipady=40,pady=40)




GUI.mainloop()