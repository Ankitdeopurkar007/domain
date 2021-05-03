from tkinter import*
import random
from tkinter import messagebox
import time


root=Tk()
root.title("Billing Software")
root.geometry("1350x700+0+0")
bg_color="#054463"



#Variable

c_name=StringVar()
c_phone=StringVar()
bill_no=StringVar()
misal_quantity=IntVar()
lassi_quantity=IntVar()
pav_quantity=IntVar()
chaas_quantity=IntVar()
final_price=StringVar()
hour=time.strftime("%H")
minute=time.strftime('%M')
second=time.strftime("%S")
day=time.strftime("%A")
x=random.randint(1000,9999)
bill_no.set(str(x))
global l
l=[]








#Function


def welcome():

    textarea.delete(1.0,END)
    textarea.insert(END,"\t Grape Embassy")
    textarea.insert(END,f'\n Current time:{time.strftime(hour)}:{time.strftime(minute)}:{time.strftime(second)}\t\t\tDay:{time.strftime(day)} ')
    textarea.insert(END,f'\n\n Bill No:\t\t{bill_no.get()}')
    textarea.insert(END,f'\n Customer Name: \t\t{c_name.get()}')
    textarea.insert(END,f'\n Phone No: \t\t{c_phone.get()}')
    textarea.insert(END,f"\n=======================================")
    textarea.insert(END,f'\n Product \t \t QTY \t\t Price')
    textarea.insert(END,f"\n=======================================\n")
    textarea.configure(font='arial 15 bold')

        
def individual_total_bill():

        welcome()

        misal=misal_quantity.get()*100
        lassi=lassi_quantity.get()*60
        chaas=chaas_quantity.get()*30
        pav=pav_quantity.get()*5

        l.append(misal)
        l.append(lassi)
        l.append(chaas)
        l.append(pav)
        

        if misal_quantity.get()!=0:

                {textarea.insert(END,f"\n Misal\t\t{misal_quantity.get()}\t\t{misal}")}
        

        if lassi_quantity.get()!=0:
                {
        textarea.insert(END,f"\n Lassi\t\t{lassi_quantity.get()}\t\t{lassi}")}
        if chaas_quantity.get()!=0:
                {
        textarea.insert(END,f"\n Chaaas\t\t{chaas_quantity.get()}\t\t{chaas}")}
        if pav_quantity.get()!=0:
                {
        textarea.insert(END,f"\n Pav\t\t{pav_quantity.get()}\t\t{pav}")}



        
         

def final_bill():
        if c_name.get()=='':
                messagebox.showerror('Error','Customer Details are Required')
        
        else:
                tex=textarea.get(10.0,(10.0+float(len(l))))
                
                welcome() 
                textarea.insert(END,tex)
        total_amount=float( misal_quantity.get()*100+
                            lassi_quantity.get()*60+
                            chaas_quantity.get()*30+
                            pav_quantity.get()*5)
        final_price.set(str(total_amount))
        
        
        textarea.insert(END,f"\n======================================")

        textarea.insert(END,f"\nTotal Amount to Pay:{total_amount}")
        textarea.insert(END,f"\n======================================")
        textarea.insert(END,f"\nTHANK YOU FOR COMING!!!!")
        textarea.insert(END,f"\nVISIT AGAIN!!")

        savebill()


def savebill():
        op=messagebox.askyesno('Save Bill','Do you want to save the Bill')
        if op>0:
                bill_details=textarea.get(1.0,END)
                f1=open("D:/bill-generator/bills/"+str(bill_no.get())+".csv",'w')
                f1.write(bill_details)
                f1.close()
                messagebox.showinfo('Saved',f'Bill No:{bill_no.get()} Saved Successfully')
        else:
                return

def clear():
        c_name.set('')
        c_phone.set('')
        misal_quantity.set(0)
        pav_quantity.set(0)
        lassi_quantity.set(0)
        chaas_quantity.set(0)
        welcome()







title=Label(root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=1).pack(fill=X)

#Customer Detail Frame
F1=LabelFrame(root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
F1.place(x=0,y=80,relwidth=1)

cname_label=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
cname_txt=Entry(F1,width=15,font="arial 15",bd=7,relief=SUNKEN,textvariable=c_name).grid(row=0,column=1,padx=10,pady=5)

cphone_label=Label(F1,text="Phone Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
cphone_txt=Entry(F1,width=15,font="arial 15",bd=7,relief=SUNKEN,textvariable=c_phone).grid(row=0,column=3,padx=10,pady=5)

 #Menu for Customers

F2=LabelFrame(root,bd=10,relief=GROOVE,text="Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
F2.place(x=5,y=180,width=325,height=380)
        
misal_label=Label(F2,text="Misal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
misal_txt=Entry(F2,width=12,font=("times new roman",16,"bold"),bd=5,textvariable=misal_quantity,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

pav_label=Label(F2,text="Extra Pav",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
lassi_txt=Entry(F2,width=12,font=("times new roman",16,"bold"),textvariable=pav_quantity,bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

lassi_label=Label(F2,text="Lassi",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
lassi_txt=Entry(F2,width=12,font=("times new roman",16,"bold"),textvariable=lassi_quantity,bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

chaas_label=Label(F2,text="Butter Milk",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
chaas_txt=Entry(F2,width=12,font=("times new roman",16,"bold"),textvariable=chaas_quantity,bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

#Bill

F3=LabelFrame(root,bd=10,relief=GROOVE)
F3.place(x=820,y=180,width=525,height=380)

bill_area=Label(F3,text="Bill Area",font=("arial 15 bold"),bd=7,relief=GROOVE).pack(fill=X)
scroll_y=Scrollbar(F3,orient=VERTICAL)
textarea=Text(F3,yscrollcommand=scroll_y.set)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=textarea.yview)
textarea.pack(fill=BOTH,expand=1)
        

#Final total of order

F5=LabelFrame(root,bd=10,relief=GROOVE,text="Total",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
F5.place(x=0,y=600,relwidth=1,height=200)

Final_Total=Label(F5,text="Total",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
final_txt=Entry(F5,width=12,font=("times new roman",16,"bold"),bd=5,textvariable=final_price,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)



F6=LabelFrame(F5,bd=10,relief=GROOVE)
F6.place(x=850,width=480,height=105)


 #Buttons

Total=Button(F6,text="Add Item",bg="cadetblue",fg="white",command=individual_total_bill,pady=15,width=11,font=("arial 15 bold")).grid(row=0,column=0,padx=5,pady=5)
Generate_Bill=Button(F6,text="Generate Bill",bg="cadetblue",command=final_bill,fg="white",pady=15,width=11,font=("arial 15 bold")).grid(row=0,column=1,padx=5,pady=5)
Clear=Button(F6,text="Clear",bg="cadetblue",fg="white",pady=15,command=clear,width=11,font=("arial 15 bold")).grid(row=0,column=2,padx=5,pady=5)

welcome()







root.mainloop()





           
           
         




        



          
        


       
        
        

        


       

       
        

        

        

     





        







        
    


        
        



