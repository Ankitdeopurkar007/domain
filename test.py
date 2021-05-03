from tkinter import*
import random
from tkinter import messagebox
import time
import tempfile
import win32api
import win32print



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
a_quantity=IntVar()
b_quantity=IntVar()
c_quantity=IntVar()
d_quantity=IntVar()
e_quantity=IntVar()
f_quantity=IntVar()
g_quantity=IntVar()
h_quantity=IntVar()
hour=time.strftime("%H")
minute=time.strftime('%M')
second=time.strftime("%S")
day=time.strftime("%A")
year=time.strftime("%Y")
x=random.randint(1000,9999)
bill_no.set(str(x))
global l
l=[]








#Function




def welcome():

    textarea.delete(1.0,END)
    textarea.insert(END,"\t Grape Embassy")
    textarea.insert(END,f'\n Current time:{time.strftime(hour)}:{time.strftime(minute)}:{time.strftime(second)}\t\tDay:{time.strftime(day)}\tYear:{time.strftime(year)} ')
    textarea.insert(END,f'\n\n Bill No:\t\t{bill_no.get()}')
    textarea.insert(END,f'\n Customer Name: \t\t{c_name.get()}')
    textarea.insert(END,f'\n Phone No: \t\t{c_phone.get()}')
    textarea.insert(END,f"\n=======================================")
    textarea.insert(END,f'\n Product \t\t QTY \t\t Price')
    textarea.insert(END,f"\n=======================================\n")
    textarea.configure(font='arial 15 bold')

    


        
def individual_total_bill():

        welcome()

        misal=misal_quantity.get()*100
        lassi=lassi_quantity.get()*60
        chaas=chaas_quantity.get()*30
        pav=pav_quantity.get()*5
        a=a_quantity.get()*5
        b=b_quantity.get()*5
        c=c_quantity.get()*5
        d=d_quantity.get()*5
        e=e_quantity.get()*5
        f=f_quantity.get()*5
        g=g_quantity.get()*5
        h=h_quantity.get()*5

        l.append(misal)
        l.append(lassi)
        l.append(chaas)
        l.append(pav)
        l.append(a)
        l.append(b)
        l.append(c)
        l.append(d)
        l.append(e)
        l.append(f)
        l.append(g)
        l.append(h)
        

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

        if a_quantity.get()!=0:
                {
        textarea.insert(END,f"\n Upwas Misal\t\t{a_quantity.get()}\t\t{a}")}

        if b_quantity.get()!=0:
                {
        textarea.insert(END,f"\n Tea\t\t{b_quantity.get()}\t\t{b}")}

        if c_quantity.get()!=0:
                {
        textarea.insert(END,f"\n Grapes Bowl\t\t{c_quantity.get()}\t\t{c}")}

        if d_quantity.get()!=0:
                {
        textarea.insert(END,f"\n Matki\t\t{d_quantity.get()}\t\t{d}")}

        if e_quantity.get()!=0:
                {
        textarea.insert(END,f"\n Shev\t\t{e_quantity.get()}\t\t{e}")}

        if f_quantity.get()!=0:
                {
        textarea.insert(END,f"\n M.Water\t\t{f_quantity.get()}\t\t{f}")}

        if g_quantity.get()!=0:
                {
        textarea.insert(END,f"\n Papad\t\t{g_quantity.get()}\t\t{g}")}

        if h_quantity.get()!=0:
                {
        textarea.insert(END,f"\n Grapes Box\t\t{h_quantity.get()}\t\t{h}")}
        



        
         

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
                            pav_quantity.get()*5+
                            a_quantity.get()*5+
                            b_quantity.get()*5+
                            c_quantity.get()*5+
                            d_quantity.get()*5+
                            e_quantity.get()*5+
                            f_quantity.get()*5+
                            g_quantity.get()*5+
                            h_quantity.get()*5)
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
                f1=open("D:/bill-generator/bills/"+str(bill_no.get())+".txt",'w')
                f1.write(bill_details)
                f1.close()
                messagebox.showinfo('Saved',f'Bill No:{bill_no.get()} Saved Successfully')
        else:
                return

def printfile():

    filename = tempfile.mktemp (".txt")
    open (filename, "w").write(textarea.get(1.0,END))
    win32api.ShellExecute (
    0,
    "print",
    filename,
  #
  # If this is None, the default printer will
  # be used anyway.
  # Addding new file
  '/d:"%s"' % win32print.GetDefaultPrinter (),
  ".",
  0
)

def clear():
        c_name.set('')
        c_phone.set('')
        bill_no.set('')
        misal_quantity.set(0)
        pav_quantity.set(0)
        lassi_quantity.set(0)
        chaas_quantity.set(0)
        a_quantity.set(0)
        b_quantity.set(0)
        c_quantity.set(0)
        d_quantity.set(0)
        e_quantity.set(0)
        f_quantity.set(0)
        g_quantity.set(0)
        h_quantity.set(0)
        final_price.set(0)
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
F2.place(x=5,y=180,width=300,height=380)
        
misal_label=Label(F2,text="Misal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
misal_txt=Entry(F2,width=5,font=("times new roman",16,"bold"),bd=5,textvariable=misal_quantity,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

pav_label=Label(F2,text="Extra Pav",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
lassi_txt=Entry(F2,width=5,font=("times new roman",16,"bold"),textvariable=pav_quantity,bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

lassi_label=Label(F2,text="Lassi",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
lassi_txt=Entry(F2,width=5,font=("times new roman",16,"bold"),textvariable=lassi_quantity,bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

chaas_label=Label(F2,text="Butter Milk",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
chaas_txt=Entry(F2,width=5,font=("times new roman",16,"bold"),textvariable=chaas_quantity,bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)


chaas_label=Label(F2,text="Upwas Misal",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
chaas_txt=Entry(F2,width=5,font=("times new roman",16,"bold"),textvariable=a_quantity,bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)


chaas_label=Label(F2,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
chaas_txt=Entry(F2,width=5,font=("times new roman",16,"bold"),textvariable=b_quantity,bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

F7=LabelFrame(root,bd=10,relief=GROOVE,text="Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
F7.place(x=350,y=180,width=300,height=380)

chaas_label=Label(F7,text="Grapes Bowl",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
chaas_txt=Entry(F7,width=5,font=("times new roman",16,"bold"),textvariable=c_quantity,bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

chaas_label=Label(F7,text="Matki",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
chaas_txt=Entry(F7,width=5,font=("times new roman",16,"bold"),textvariable=d_quantity,bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

chaas_label=Label(F7,text="Shev",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
chaas_txt=Entry(F7,width=5,font=("times new roman",16,"bold"),textvariable=e_quantity,bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

chaas_label=Label(F7,text="M.Water",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
chaas_txt=Entry(F7,width=5,font=("times new roman",16,"bold"),textvariable=f_quantity,bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

chaas_label=Label(F7,text="Papad",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
chaas_txt=Entry(F7,width=5,font=("times new roman",16,"bold"),textvariable=g_quantity,bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

chaas_label=Label(F7,text="Grapes Box",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=10,pady=10,sticky="w")
chaas_txt=Entry(F7,width=5,font=("times new roman",16,"bold"),textvariable=h_quantity,bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

#Bill

F3=LabelFrame(root,bd=10,relief=GROOVE)
F3.place(x=920,y=180,width=525,height=380)

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
F6.place(x=750,width=630,height=105)


 #Buttons

Total=Button(F6,text="Add Item",bg="cadetblue",fg="white",command=individual_total_bill,pady=15,width=11,font=("arial 15 bold")).grid(row=0,column=0,padx=5,pady=5)
Generate_Bill=Button(F6,text="Generate Bill",bg="cadetblue",command=final_bill,fg="white",pady=15,width=11,font=("arial 15 bold")).grid(row=0,column=1,padx=5,pady=5)
Clear=Button(F6,text="Clear",bg="cadetblue",fg="white",pady=15,command=clear,width=11,font=("arial 15 bold")).grid(row=0,column=2,padx=5,pady=5)
Print=Button(F6,text="Print",bg="cadetblue",fg="white",pady=15,command=printfile,width=11,font=("arial 15 bold")).grid(row=0,column=3,padx=5,pady=5)

welcome()







root.mainloop()





           
           
         




        



          
        


       
        
        

        


       

       
        

        

        

     





        







        
    


        
        



