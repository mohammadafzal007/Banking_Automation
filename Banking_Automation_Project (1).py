#!/usr/bin/env python
# coding: utf-8

# In[6]:


from tkinter import *
from tkinter.ttk import Combobox
import sqlite3
from datetime import datetime
import time
from tkinter import messagebox
from tkinter.ttk import Style,Treeview,Scrollbar
import re

try:
   conobj=sqlite3.connect(database='banking.sqlite')
   curobj=conobj.cursor()
   curobj.execute('create table accounts(acno integer primary key autoincrement,name text,email text,mobile text,password text,balance float,acctype text,opendate text)')
   curobj.execute('create table txns(acno int,amount float,updatebalance float,txntype text,txndate text)')
   conobj.close()
   print('Table Created')
except:
    print('Something Wrong')
win=Tk()
win.state('zoomed')
win.title('Banking Automation')
win.configure(bg='#FF6103')
win.resizable(height=False,width=False)
title=Label(text=' Banking Automation ',font=('arial',50,'bold','underline'),bg='#FF6103',fg='#FFD800')
title.pack()
# l1=Label(win,text='afzal',font=('arial',10,'bold'),fg='red')
# l1.place(relx=0.84,rely=0.08)
# def showtime():
#     now=datetime.now()
#     mytime=now.strftime("%B %d ,%Y %I:%M:%S %p")
#     l1.config(text=mytime)
#     l1.after(1000,time)

def mainscreen():
    # showtime()
    frm=Frame(win)
    frm.place(relx=0,rely=.12,relheight=.9,relwidth=1)
    frm.configure(bg='cornsilk3')
       
    def newacc():
        frm.destroy()
        newaccframe() 
    def fpw():
        frm.destroy()
        fpframe()

    def login():
        acno=entry_acn.get()
        password=entry_password.get()
        if len(acno)==0 or len(password)==0:
            messagebox.showerror('Required ','All Fields Required')
        else:
           conobj=sqlite3.connect(database='banking.sqlite')
           curobj=conobj.cursor()
           curobj.execute('select * from accounts where acno=? and password=?',(acno,password))
           res=curobj.fetchone()
           if res==None:
               messagebox.showerror('Account Not Exist','Invalid A/c No and Password')
           else:
               global uacno,uname
               uacno=res[0]
               uname=res[1]
               frm.destroy()
               loginframe() 
    def clear_text():
       entry_acn.delete(0, END)
       entry_password.delete(0, END)
    Lbl_acn=Label(frm,text='A/C No. ',font=('arial',20,'italic'),bg='cornsilk3')
    Lbl_acn.place(relx=.3,rely=.2)

    entry_acn=Entry(frm,font=('arial',20,'italic'),bd=5)
    entry_acn.place(relx=.4,rely=.2)
    entry_acn.focus()

    Lbl_password=Label(frm,text='Password',font=('arial',20,'italic'),bg='cornsilk3',)
    Lbl_password.place(relx=.3,rely=.3)

    entry_password=Entry(frm,font=('arial',20,'italic'),bd=5,show='*')
    entry_password.place(relx=.4,rely=.3)

    login_btn=Button(frm,text='Log in',font=('arial',20,'bold'),command=login)
    login_btn.place(relx=.43,rely=.4)
    
    reset_btn=Button(frm,command=clear_text ,text='Reset',font=('arial',20,'bold'))
    reset_btn.place(relx=.53,rely=.4)

    fgt_btn=Button(frm,text='Forgot Password ?',font=('arial',20,'bold'),command=fpw)
    fgt_btn.place(relx=.42,rely=.6)

    newacc_btn=Button(frm,text='Sign Up',font=('arial',20,'bold'),command=newacc)
    newacc_btn.place(relx=.47,rely=.7)
   
        
    
def newaccframe():
    frm=Frame(win)
    frm.place(relx=0,rely=.12,relheight=.9,relwidth=1)
    frm.configure(bg='cornsilk3')

    def back():
        frm.destroy()
        mainscreen() 
    def newacc():
        namepattern=r'^[^\d_]+$'
        emailpattern=r'^([a-zA-Z_])\w.*@(gmail|email)\.\w+'
        mobilepattern=r'^(\+\d{1,3}[- ]?)?\d{10}$'
        name=entry_name.get()
        email=entry_email.get()
        mobile=entry_mobile.get()
        password=entry_password.get()
        balance=0
        acctype=cbtype.get()
        opendate=time.ctime()
        if re.search(namepattern,name) and re.search(emailpattern,email) and re.search(mobilepattern,mobile):
                  conobj=sqlite3.connect(database='banking.sqlite')
                  curobj=conobj.cursor()
                  curobj.execute('insert into accounts(name,email,mobile,password,balance,acctype,opendate) values(?,?,?,?,?,?,?)',(name,email,mobile,password,balance,acctype,opendate))
                  conobj.commit()
                  curobj.close()

                  curobj=conobj.cursor()
                  curobj.execute('select acno,name from accounts where acno =(select max(acno) from accounts)')
                  res=curobj.fetchone()
                  messagebox.showinfo('Account Created',f'Congratulation {res[1]} Your Account is created Your A/C No is {res[0]}')
                  conobj.close()
        else:
            messagebox.showerror('Invalid Validation','Not Valid Name Mobile and Email')
    Lbl_name=Label(frm,text='Name',font=('arial',20,'italic'),bg='cornsilk3')
    Lbl_name.place(relx=.3,rely=.1)

    entry_name=Entry(frm,font=('arial',20,'italic'),bd=5)
    entry_name.place(relx=.4,rely=.1)
    entry_name.focus()

    Lbl_email=Label(frm,text='E-mail',font=('arial',20,'italic'),bg='cornsilk3')
    Lbl_email.place(relx=.3,rely=.2)

    entry_email=Entry(frm,font=('arial',20,'italic'),bd=5)
    entry_email.place(relx=.4,rely=.2)

    Lbl_mobile=Label(frm,text='Mobile.',font=('arial',20,'italic'),bg='cornsilk3')
    Lbl_mobile.place(relx=.3,rely=.3)

    entry_mobile=Entry(frm,font=('arial',20,'italic'),bd=5)
    entry_mobile.place(relx=.4,rely=.3)

    Lbl_password=Label(frm,text='Password',font=('arial',20,'italic'),bg='cornsilk3')
    Lbl_password.place(relx=.3,rely=.4)

    entry_password=Entry(frm,font=('arial',20,'italic'),bd=5,show='*')
    entry_password.place(relx=.4,rely=.4)

    Lbl_acctype=Label(frm,text='A/C Type',font=('arial',20,'italic'),bg='cornsilk3')
    Lbl_acctype.place(relx=.3,rely=.5)

    cbtype=Combobox(frm,values=['Saving','Current'],font=('arial',20,'bold'))
    cbtype.current(0)
    cbtype.place(relx=.4,rely=.5)

    createacc_btn=Button(frm,command=newacc,text='Sign Up',font=('arial',20,'bold'))
    createacc_btn.place(relx=.45,rely=.6)

    back_btn=Button(frm,text='⬅',font=('arial',20,'bold'),command=back)
    back_btn.place(relx=0.01,rely=0.01)
 

def fpframe():
    frm=Frame(win)
    frm.place(relx=0,rely=.12,relheight=.9,relwidth=1)
    frm.configure(bg='cornsilk3')

    def back():
        frm.destroy()
        mainscreen()
    def recoverpwd():
     acno=entry_acn.get()
     mobile=entry_mobile.get()
     email=entry_email.get()
     conobj=sqlite3.connect(database='banking.sqlite')
     curobj=conobj.cursor()
     curobj.execute('select password from accounts where acno=? and mobile=? and email=?',(acno,mobile,email))
     res=curobj.fetchone()
     if res==None:
         messagebox.showerror('Forgot Password','Account Not Found') 
     else:
         messagebox.showinfo('Forgot Password',f'Your Password is {res[0]}')
    def clear_text():
       entry_acn.delete(0, END)
       entry_mobile.delete(0, END)    
       entry_email.delete(0, END)       
    Lbl_acn=Label(frm,text='A/C No. ',font=('arial',20,'italic'),bg='cornsilk3')
    Lbl_acn.place(relx=.3,rely=.2)

    entry_acn=Entry(frm,font=('arial',20,'italic'),bd=5)
    entry_acn.place(relx=.4,rely=.2)
    entry_acn.focus()

    Lbl_mobile=Label(frm,text='Mobile.',font=('arial',20,'italic'),bg='cornsilk3')
    Lbl_mobile.place(relx=.3,rely=.3)

    entry_mobile=Entry(frm,font=('arial',20,'italic'),bd=5)
    entry_mobile.place(relx=.4,rely=.3) 
    
    Lbl_email=Label(frm,text='Email',font=('arial',20,'italic'),bg='cornsilk3')
    Lbl_email.place(relx=.3,rely=.4)

    entry_email=Entry(frm,font=('arial',20,'italic'),bd=5)
    entry_email.place(relx=.4,rely=.4 )
                    
    changepwd_btn=Button(frm,command=recoverpwd,text='Get Password',font=('arial',20,'bold'))
    changepwd_btn.place(relx=.33,rely=.6)

    reset_btn=Button(frm,command=clear_text,text='Reset',font=('arial',20,'bold'))
    reset_btn.place(relx=.55,rely=.6)
    
    back_btn=Button(frm,text='⬅',font=('arial',20,'bold'),command=back)
    back_btn.place(relx=0.01,rely=0.01)

def loginframe():
    frm=Frame(win)
    frm.place(relx=0,rely=.12,relheight=.9,relwidth=1)
    frm.configure(bg='cornsilk3')
    
    def logout():
        frm.destroy()
        conobj.close()
        mainscreen()

    def detailsscreen():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.place(relx=0.3,rely=0.2,relwidth=0.6,relheight=0.6)
        ifrm_title=Label(ifrm,text='Account Details',font=('arial',20,'bold','underline'))
        ifrm_title.pack()

        conobj=sqlite3.connect(database='banking.sqlite')
        curobj=conobj.cursor()
        curobj.execute('select * from accounts where acno=?',(uacno,))
        res=curobj.fetchone()
        acno=res[0]
        name=res[1]
        email=res[2]
        mobile=res[3]
        balance=res[5]
        l1=Label(ifrm,text=f'A/c Number      {acno}',font=('arial',20,'bold'),fg='green')
        l1.place(relx=.2,rely=.2)
        l1=Label(ifrm,text=f'Name                {name}',font=('arial',20,'bold'),fg='green')
        l1.place(relx=.2,rely=.3)
        l1=Label(ifrm,text=f'Balance              {balance}',font=('arial',20,'bold'),fg='green')
        l1.place(relx=.2,rely=.4)

    
        
    
        
    def depositscreen():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.place(relx=0.3,rely=0.2,relwidth=0.6,relheight=0.6)
        ifrm_title=Label(ifrm,text='Deposit Amount',font=('arial',20,'bold','underline'))
        ifrm_title.pack()
        # curobj.execute('create table txns(acno int,amount float,updatebalance float,txntype text,txndate text)')
        
        def depositamount():
            depositamount=float(entry_deposit.get())
            txndate=time.ctime()
            conobj=sqlite3.connect(database='banking.sqlite')
            curobj=conobj.cursor()
            curobj.execute('select balance from accounts where acno =?',(uacno,))
            bal=curobj.fetchone()[0]
            curobj.close()
            curobj=conobj.cursor()
            curobj.execute('update accounts set balance=balance+? where acno=?',(depositamount,uacno))
            curobj.execute('insert into txns values(?,?,?,?,?)',(uacno,depositamount,depositamount+bal,'Credit',txndate))
            conobj.commit()
            conobj.close()
            messagebox.showinfo('Success',f'Deposit Successfully Your Available Balance:{depositamount+bal}')
     
        l1_deposit=Label(ifrm,text='Deposit Amount ',font=('arial',20,'bold'))
        l1_deposit.place(relx=.17,rely=.3)
        
        entry_deposit=Entry(ifrm,font=('arial',20,'italic'),bd=5)
        entry_deposit.place(relx=.5,rely=.3 )
        
        deposit_amt_btn=Button(ifrm,text='Deposit',font=('arial',20,'bold'),bd=5,command=depositamount)
        deposit_amt_btn.place(relx=0.4,rely=0.5)
    def withdrawscreen():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.place(relx=0.3,rely=0.2,relwidth=0.6,relheight=0.6)
        ifrm_title=Label(ifrm,text='Withdraw Amount',font=('arial',20,'bold','underline'))
        ifrm_title.pack()
        def withdrawamount():
            withdrawamount=float(entry_withdraw.get())
            txndate=time.ctime()
            conobj=sqlite3.connect(database='banking.sqlite')
            curobj=conobj.cursor()
            curobj.execute('select balance from accounts where acno =?',(uacno,))
            bal=curobj.fetchone()[0]
            totalbal=bal-withdrawamount
            curobj.close()
            if bal<withdrawamount:
                messagebox.showwarning('Warning',f'Insufficient Balance :{bal} ')
            else:
                 curobj=conobj.cursor()
                 curobj.execute('update accounts set balance=? where acno=?',(totalbal,uacno))
                 curobj.execute('insert into txns values(?,?,?,?,?)',(uacno,withdrawamount,totalbal,'Debit',txndate))
                 conobj.commit()
                 conobj.close()
                 messagebox.showinfo('Success',f'Withdrawal Successfully Your Available Balance:{totalbal}')
        l1_withdraw=Label(ifrm,text='Withdraw Amount ',font=('arial',20,'bold'))
        l1_withdraw.place(relx=.17,rely=.3)
        
        entry_withdraw=Entry(ifrm,font=('arial',20,'italic'),bd=5)
        entry_withdraw.place(relx=.5,rely=.3 )
        
        withdraw_amt_btn=Button(ifrm,text='Withdraw',font=('arial',20,'bold'),bd=5,command=withdrawamount)
        withdraw_amt_btn.place(relx=0.4,rely=0.5)
    def historyscreen():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.place(relx=0.3,rely=0.2,relwidth=0.6,relheight=0.6)
        ifrm_title=Label(ifrm,text='Transaction History',font=('arial',20,'bold','underline'))
        ifrm_title.pack()
        
        tv=Treeview(ifrm)
        tv.place(x=10,y=60,height=300,width=800)

        sb=Scrollbar(ifrm,orient='vertical',command=tv.yview)
        sb.place(x=780,y=65,height=285)
        tv.configure(yscrollcommand=sb.set)

        style=Style()
        style.configure('Treeview.Heading',font=('arial',10,'bold'),fg='blue')
        
        tv['columns']=('Sr.No','txndate','txntype','amt','upbal')
        tv.column('Sr.No',width=100,anchor='c')
        tv.column('txndate',width=100,anchor='c')
        tv.column('amt',width=100,anchor='c')
        tv.column('upbal',width=100,anchor='c')
        tv.column('txntype',width=100,anchor='c')


        tv.heading('Sr.No',text='Sr.No')
        tv.heading('txndate',text='Transaction Date')
        tv.heading('amt',text='Amount')
        tv.heading('upbal',text='Balance')
        tv.heading('txntype',text='Transaction Type')

        tv['show']='headings'

        conobj=sqlite3.connect(database='banking.sqlite')
        curobj=conobj.cursor()
        curobj.execute('Select * from txns where acno=?',(uacno,))
        count=0
        for res in curobj:
            count=count+1
            tv.insert('','end',values=(count,res[4],res[3],res[1],res[2]))
            
                        

    def transferscreen():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.place(relx=0.3,rely=0.2,relwidth=0.6,relheight=0.6)
        ifrm_title=Label(ifrm,text='Transfer Amount',font=('arial',20,'bold','underline'))
        ifrm_title.pack()
        def transfer():
            toaccount=entry_toaccount.get()
            amount=float(entry_amount.get())
            txndate=time.ctime()
            conobj=sqlite3.connect(database='banking.sqlite')
            curobj=conobj.cursor()
            curobj.execute('select * from accounts where acno=?',(toaccount,))
            res=curobj.fetchone()
            tobal=res[5]
            tobaltotal=tobal+amount
            curobj.close()
            if res==None:
                messagebox.showinfo('Account','Account Not Exist')
            else:
                curobj=conobj.cursor()
                curobj.execute('select balance from accounts where acno=?',(uacno,))
                bal=curobj.fetchone()[0]
                totalbal=bal-amount
                curobj.close()
                if bal<amount:
                      messagebox.showwarning('Transfer',f'Insufficient Balance : Rs {bal}')
                else:
                      curobj=conobj.cursor()
                      curobj.execute('update accounts set balance=? where acno=?',(tobaltotal ,toaccount))
                      curobj.execute('update accounts set balance=? where acno=?',(totalbal ,uacno))
                      curobj.execute('insert into txns values(?,?,?,?,?)',(uacno,amount,totalbal,'Debit',txndate))
                      curobj.execute('insert into txns values(?,?,?,?,?)',(toaccount,amount,tobaltotal,'Credit',txndate))
                      conobj.commit()
                      conobj.close()
                      messagebox.showinfo('Transfer ',f'''Rs {amount} Transfer Successfully to account no {toaccount} ,
                      Your Available Balance : Rs {totalbal}''')

                      
        lbl_toaccount=Label(ifrm,text='To Account',font=('arial',20,'bold'),bg='white')
        lbl_toaccount.place(relx=0.2,rely=0.2)
        entry_toaccount=Entry(ifrm,font=('arial',20,'bold'))
        entry_toaccount.place(relx=0.4,rely=0.2)
        
        lbl_amount=Label(ifrm,text='Amount',font=('arial',20,'bold'),bg='white')
        lbl_amount.place(relx=0.2,rely=0.35)
        entry_amount=Entry(ifrm,font=('arial',20,'bold'))
        entry_amount.place(relx=0.4,rely=0.35)

        lbl_amount=Button(ifrm,command=transfer ,text='Transfer',font=('arial',20,'bold'),bg='white')
        lbl_amount.place(relx=0.45,rely=0.5)
    def updateprofilescreen():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.place(relx=0.3,rely=0.2,relwidth=0.6,relheight=0.6)
        ifrm_title=Label(ifrm,text='Update Profile',font=('arial',20,'bold','underline'))
        ifrm_title.pack()
        def updateprofile():
            name=entry_name.get()
            mobile=entry_mobile.get()
            email=entry_email.get()
            password=entry_password.get()
            conobj=sqlite3.connect(database='banking.sqlite')
            curobj=conobj.cursor()
            
            curobj.execute('update accounts set name=?,mobile=?,email=?,password=? where acno=?',(name,mobile,email,password,uacno))
            conobj.commit()
            messagebox.showinfo('Update','Profile Updated Successfully')
            ifrm.destroy()
            # global uname
            # uname=name
            updateprofilescreen()
        # call function when we click on entry box def click(*args): 
        lbl_name=Label(ifrm,text='Name',font=('arial',20,'bold'),bg='white')
        lbl_name.place(relx=0.2,rely=0.2)
        entry_name=Entry(ifrm,font=('arial',20,'bold'))
        entry_name.place(relx=0.4,rely=0.2)
        lbl_mobile=Label(ifrm,text='Mobile',font=('arial',20,'bold'),bg='white')
        lbl_mobile.place(relx=0.2,rely=0.33)
        entry_mobile=Entry(ifrm,font=('arial',20,'bold'))
        entry_mobile.place(relx=0.4,rely=0.33)
        lbl_email=Label(ifrm,text='E-mail',font=('arial',20,'bold'),bg='white')
        lbl_email.place(relx=0.2,rely=0.46)
        entry_email=Entry(ifrm,font=('arial',20,'bold'))
        entry_email.place(relx=0.4,rely=0.46)
        lbl_password=Label(ifrm,text='Password',font=('arial',20,'bold'),bg='white')
        lbl_password.place(relx=0.2,rely=0.59)
        entry_password=Entry(ifrm,font=('arial',20,'bold'))
        entry_password.place(relx=0.4,rely=0.59)

        Update_btn=Button(frm,text='Update Profile',font=('arial',20,'bold'),command=updateprofile)
        Update_btn.place(relx=0.5,rely=0.65)
        conobj=sqlite3.connect(database='banking.sqlite')
        curobj=conobj.cursor()
        curobj.execute('select * from accounts where acno=?',(uacno,))
        res=curobj.fetchone()
        curobj.close()
        entry_name.insert('0',res[1])
        entry_email.insert('0',res[2])
        entry_mobile.insert('0',res[3])
        entry_password.insert('0',res[4])

    lbl_welcome=Label(frm,text=f'Welcome,{uname}',font=('arial',20,'bold'),fg='red',bg='cornsilk3')
    lbl_welcome.place(relx=0,rely=0.02)
    
    lbl_welcomefull=Label(frm,text=f'''Welcome, {uname} 
    to Banking Automation ''',font=('arial',30,'bold'),fg='red',bg='cornsilk3')
    lbl_welcomefull.place(relx=0.4,rely=0.3)
    
    logout_btn=Button(frm,text='Log Out',font=('arial',20,'bold'),command=logout)
    logout_btn.place(relx=0.9,rely=0.01)

    account_details_btn=Button(frm,text='Account Details',font=('arial',20,'bold'),command=detailsscreen,width=15)
    account_details_btn.place(relx=0,rely=0.2)

    update_profile_btn=Button(frm,text='Update Profile',font=('arial',20,'bold'),command=updateprofilescreen,width=15)
    update_profile_btn.place(relx=0,rely=0.3)
    
    deposit_btn=Button(frm,text='Deposit',font=('arial',20,'bold'),command=depositscreen,width=15)
    deposit_btn.place(relx=0,rely=0.4)
    
    withdraw_btn=Button(frm,text='Withdraw',font=('arial',20,'bold'),command=withdrawscreen,width=15)
    withdraw_btn.place(relx=0,rely=0.5)

    transfer_btn=Button(frm,text='Transfer',font=('arial',20,'bold'),command=transferscreen,width=15)
    transfer_btn.place(relx=0,rely=0.6) 
    
    history_btn=Button(frm,text='History',font=('arial',20,'bold'),command=historyscreen,width=15)
    history_btn.place(relx=0,rely=0.7)
    
mainscreen()
win.mainloop()


# In[30]:






# In[45]:





# In[ ]:




