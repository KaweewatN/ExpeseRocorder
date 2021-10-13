from tkinter import *
from tkinter import ttk, messagebox 
import csv
from datetime import datetime

GUI = Tk()
GUI.title ('โปรแกรมบันทึกค่าใช้จ่าย by TK')
GUI.geometry('600x700+500+50')
############## Menu bar ################
menubar = Menu(GUI)
GUI.config(menu=menubar) #GUI.config ทำให้ menubar ไปติดกับ GUI

# File menu
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label = 'File',menu=filemenu)
filemenu.add_command(label = 'Import CSV')
filemenu.add_command(label = 'Export to Google Sheet')

#Help
def About():
    messagebox.showinfo('About','สวัสดีครับ โปรแกรมนี้คือโปรแกรมบันทึกข้อมูล\nบริจาค 1 BTC ให้เด็กน้อยนะครับ') 
    # def ต้องอยู่ข้างบนเท่านั้น
helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label = 'Help',menu=helpmenu)
helpmenu.add_command(label = 'About',command= About)

def Donate():
    messagebox.showinfo('Donate','อยากได้ etherium จังเลยช่วยบริจาคหน่อยได้มั้ย')

#Donate
donatemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label = 'Donate',menu=donatemenu)
donatemenu.add_command(label = 'Please Donate',command = Donate)

#################################################

icon_t1=PhotoImage(file='T1.expense.png')
icon_t2=PhotoImage(file='T2.expense.png')

Tab=ttk.Notebook(GUI)
T1=Frame(Tab) #สามารถใส่ width,height ได้
T2=Frame(Tab) # GUI TAB FRAME LABEL E1,E2
Tab.pack(fill=BOTH,expand=1)

Tab.add(T1,text= f'{"เพิ่มรายการ":^{30}}',image=icon_t1,compound='top') # ใช้ Tab.add(T1,text='   เพิ่มรายการ  ') ได้
# .subsample(2) = ย่อรูป
Tab.add(T2,text= f'{"ค่าใช้จ่ายทั้งหมด":^{30}}',image=icon_t2,compound='top') # >ขวา < ซ้าย ^กลาง

F1=Frame(T1) #ใส่ Frame(GUI)ได้
F1.pack() #F1.place(x=100,y=50)

days={'Mon':'จันทร์', 'Tue':'จันทร์', 'Wed':'พุธ','Thu':'พฤหัส','Fri':'ศุกร์','Sat':'เสาร์','Sun':'อาทิตย์'}

def Save(event=None):
    expense = v_expense.get() 
    price = v_price.get()
    quantity = v_quantity.get()
    if expense == '':
        print('No Data')
        messagebox.showwarning('Error','กรุณากรอกรายการค่าใช้จ่าย')
        return # ทำให้จบ function
    elif price == '':
        print('No Data')
        messagebox.showwarning('Error','กรุณากรอกราคา (บาท)')
        return  
    elif quantity == '':
        print('No Data')
        messagebox.showwarning('Error','กรุณากรอกจำนวนที่ซื้อ')   
        return
    #elif quantity == '':
        #print('No Data')
        #quantity = 1 
           
    try:
        total = int(price)*int(quantity)
        print(f'รายการ: {expense} ราคา: {price} บาท')
        print(f'จำนวนชิ้น: {quantity} ราคารวม: {total} บาท')
        text1 = f'รายการ: {expense} ราคา: {price} บาท\n'
        text2 = text1 + f'จำนวนที่ซื้อ: {quantity} ราคารวม: {total} บาท'
        v_result.set(text2)
        v_expense.set('')
        v_price.set('')
        v_quantity.set('')
        today = datetime.now().strftime('%a') #datetime.now() = today %a = day in a week ,day['Mon'] = 'จันทร์'
        dt = datetime.now().strftime ('%Y-%m-%d-%H:%M:%S')  
        date = days[today] + '-' + dt
        with open('Savee.csv','a',encoding='utf-8',newline='') as f:
            fw = csv.writer(f) 
            data = [date,expense,price,quantity,total]
            fw.writerow(data)
         
        E1.focus()
        update_table()

    except Exception as e:
        print('ERROR',e)
        messagebox.showwarning('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกข้อมูลผิด')
        #messagebox.showerror('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกข้อมูลผิด')
        #messagebox.showinfo('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกข้อมูลผิด')
        v_expense.set('')
        v_price.set('')
        v_quantity.set('') # เคลียร์ข้อมูลเก่า

GUI.bind('<Return>',Save) 

FONT1=('Angsna New',20) 
FONT2=(None,18)

main_icon = PhotoImage(file='money.png')
Mainicon = Label(F1,image=main_icon)
Mainicon.pack()

L1= ttk.Label(F1,text='รายการค่าใช้จ่าย',font=FONT1).pack()
v_expense = StringVar() #ใช้ FloatVar()ได้
E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT2)
E1.pack()

L2= ttk.Label(F1,text='ราคา (บาท)',font=FONT1).pack()
v_price = StringVar()
E2 = ttk.Entry(F1,textvariable=v_price,font=FONT2)
E2.pack()

L3= ttk.Label(F1,text='จำนวนที่ซื้อ',font=FONT1).pack()
v_quantity = StringVar()
E3= ttk.Entry(F1,textvariable=v_quantity,font=FONT2)
E3.pack()

icon_b1 = PhotoImage(file = 'B.save.png')
B2 = ttk.Button(F1,text=f'{"Save": >{10}}',image = icon_b1,compound ='left',command=Save) 
B2.pack(ipadx=50,ipady=20,pady=20) 

v_result = StringVar()
v_result.set('--------ผลลัพธ์--------')
result = ttk.Label(F1,textvariable=v_result,font=FONT1,foreground='#339EFF') #blue ก็ได้ #339EFF ก็ได้
#result = Label(F1,textvariable=v_result,font=FONT1,fg='blue')
result.pack(pady=20)

############################TAB2################################
#rs = []

def read_csv():
    #global rs 
    with open('Savee.csv',encoding='utf-8',newline='') as f: #a+ สำหรับ open and read files
        reader = csv.reader(f)
        data = list(reader)
        # rs = data 
        # print(rs) แบบ global rs
        # print(data)
        # print(------------)
        # print(data[0][0])
        # for d in data:
            # print(e) #print(d[0]) ได้ show listที่ 1
        # for a,b,c,d,e in data:
            # print(b) วิธีนี้ก็ได้
    return data # ถ้าไม่ return จะขึ้น None #return เพื่อนำข้อมูลไปใช้ต่อ       
                # function ต้องมี return เสมอ
#rs = read_csv()
#print(rs) แบบ return data

######table########

L4= ttk.Label(T2,text='ตารางแสดงผลลัพธ์ทั้งหมด',font=FONT1).pack(pady=20) #ถ้าใช้ต่อต้องใช้ L4.pack()

header = ['วัน-เวลา','รายการ','ค่าใช้จ่าย','จำนวน','รวม']
resulttable = ttk.Treeview(T2,columns=header,show='headings',height=10) #show='headings' ทำให้ผลลัพท์เป็น Heading
resulttable.pack()

# resulttable.heading(header[0],text = header[0]) #text = 'วัน-เวลา'ก็ได้
# resulttable.heading(header[1],text = header[1])
# resulttable.heading(header[2],text = header[2])
# resulttable.heading(header[3],text = header[3])
# resulttable.heading(header[4],text = header[4])

# for i in range(len(header)):
    #resulttable.heading(header[i],text = header[i])

for h in header:
    resulttable.heading(h,text = h)

headerwidth = [150,170,80,80,80]

# ใช้ resulttable.column('วัน-เวลา',width=100) แบบ mannual ได้

for h,w in zip(header,headerwidth):
    resulttable.column(h,width=w)

#resulttable.insert('','0',value=['Mon','น้ำดื่ม',30,5,150])
#resulttable.insert('','end',value=['Tue','น้ำดื่ม',30,5,150]) #ใส่ 0 ให้ Tue อยู่ก่อน

def update_table():
    resulttable.delete(*resulttable.get_children()) # delete ค่าก่อนมีการ update table
    #for c in resulttable.get_children():
        #resulttable.delete(c) สามารถใช้ได้
    data = read_csv()
    for d in data:
        resulttable.insert('','0',value=d)

update_table()
print('GET CHILD:',resulttable.get_children())

GUI.mainloop()