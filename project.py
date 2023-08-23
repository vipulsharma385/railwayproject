
#                         RAILWAY RESERVATION PROJECT USING PYTHON AND MYSQL

import os
                                     #SIGN-IN FUNCTION
def signin():
        os.system('cls')
        print("\t\t\t  -------------------------------------------")
        print("\t\t\t |               SIGN IN PAGE                |")
        print("\t\t\t  -------------------------------------------")
        a=input("\t\t\t\t     USERNAME: ")
        b=input("\t\t\t\t     PASSWORD: ")
        s="Select user_name from user_accounts where password='{}'".format(b)
        cursor.execute(s)
        data=cursor.fetchone()
        if data[0]==a:
             print("\t\t--------------------------------------------------------------")        
             print("\t\t\t\t    LOGGED IN SUCCESSFULLY")
             print("\t\t--------------------------------------------------------------")       
             main()
        else:
             print("ACCOUNT DOES NOT EXISTS OR WRONG ENTRY")      

                                        #SIGN-UP FUNCTION
def signup():
     os.system('cls')
     print("\t\t\t  -------------------------------------------")
     print("\t\t\t |               SIGN UP PAGE                |")
     print("\t\t\t  -------------------------------------------")
     f=input("\t\t\t     FIRST NAME: ")
     l=input("\t\t\t     LAST NAME: ")
     a=input("\t\t\t     USERNAME: ")
     b=input("\t\t\t     PASSWORD: ")
     c=input("\t\t\t     RE-ENTER YOUR PASSWORD: ")
     ph=input("\t\t\t     PHONE NUMBER: ")
     print('\t\t\t     M=MALE','F=FEMALE','N=NOT TO MENTION')
     gen=input("\t\t\t     ENTER YOUR GENDER: ")
     print("\t\t\t     ENTER YOUR DOB: ")
     d=input("\t\t\t     DD: ")
     o=input("\t\t\t     MM: ")
     p=input("\t\t\t     YYYY: ")
     dob=d+'/'+o+'/'+p
     age=input("\t\t\t     ENTER YOUR AGE: ")
     v={'m':'MALE','f':'FEMALE','n':'NOT TO MENTION'}
     if b==c:
          c1="insert into user_accounts values('{}','{}','{}','{}','{}','{}','{}','{}')".format(f,l,a,b,ph,v[gen],dob,age)
          cursor.execute(c1)
          print("\t\t--------------------------------------------------------------")        
          print("\t\t\t\t    ACCOUNT CREATED SUCCESSFULLY")
          print("\t\t--------------------------------------------------------------")       
     else:
          print("PASSWORD DID NOT MATCH")

                                     #TICKET BOOKING FUNCTION
def ticket_book():
     print("\t\t\t  -------------------------------------------")
     print("\t\t\t |               TICKET BOOKING              |")
     print("\t\t\t  -------------------------------------------")
     nm=input('\t\t\t     ENTER YOUR NAME: ')
     phno=input('\t\t\t     ENTER YOUR PHONE NUMBER: ')
     age=int(input('\t\t\t     ENTER YOUR AGE: '))
     print('\t\t\t     M=MALE','\t','F=FEMALE','\t','N=NOT TO MENTION')
     gender=input("\t\t\t     ENTER YOUR GENDER: ")
     Gender=gender.upper()
     fr=input('\t\t\t     ENTER YOUR STARTING POINT: ')
     to=input('\t\t\t     ENTER YOUR DESTINATION: ')
     print("\t\t\t     ENTER YOUR DOB: ")
     date1=input("\t\t\t     DD: ")
     date2=input("\t\t\t     MM: ")
     date3=input("\t\t\t     YYYY: ")
     date=date1+"/"+date2+"/"+date3
     a={'M':'MALE','F':'FEMALE','N':'NOT TO MENTION'}
     v=a[Gender]
     s1="insert into railway values('{}','{}','{}','{}','{}','{}','{}')".format(nm,phno,age,v,fr,to,date)
     cursor.execute(s1)
     print("\t\t--------------------------------------------------------------")        
     print("\t\t\t\t    TICKET BOOKED SUCCESSFULLY")
     print("\t\t--------------------------------------------------------------")       

                                   #TICKET CHECKING FUNCTION
def ticket_check():
     print("\t\t\t  -------------------------------------------")
     print("\t\t\t |               TICKET CHECKING             |")
     print("\t\t\t  -------------------------------------------")
     phno=int(input('\t\t\t     ENTER PHONE NUMBER: '))
     try:
          s1=("select * from railway where phno='{}'".format(phno))
          cursor.execute(s1)
          data=cursor.fetchone()
          Data=list(data)
          a=['NAME','PHONE NUMBER','AGE','GENDER','STARTING POINT','DESTINATION','DATE']
          print('\n\t\t\t\t\t  TICKET INFORMATION')
          print('\t\t\t\t\t  ------------------\n')
          print("\t\t\t\t\t |",a[0],"-->",Data[0])
          print("\t\t\t\t\t |",a[1],"-->",Data[1])
          print("\t\t\t\t\t |",a[2],"-->",Data[2])
          print("\t\t\t\t\t |",a[3],"-->",Data[3])     
          print("\t\t\t\t\t |",a[4],"-->",Data[4])
          print("\t\t\t\t\t |",a[5],"-->",Data[5])
          print("\t\t\t\t\t |",a[6],"-->",Data[6],"\n")
     except:
          print("TICKET DOES NOT EXIST")

                                   #TICKET CANCELLATION FUNCTION 
def ticket_cancel():
     print("\t\t\t  -------------------------------------------")
     print("\t\t\t |             TICKET CANCELLATION           |")
     print("\t\t\t  -------------------------------------------")
     phno=input('\t\t\t     ENTER YOUR PHONE NUMBER: ')
     s="Select phno from railway where phno='{}'".format(phno)
     cursor.execute(s)
     data=cursor.fetchone()
     if data[0]==phno:
          s1='delete from railway where phno=phno'
          cursor.execute(s1)
          print("\t\t--------------------------------------------------------------")        
          print("\t\t\t\t    TICKET CANCELLED SUCCESSFULLY")
          print("\t\t--------------------------------------------------------------")       
          main()
     else:
          print('TICKET DOES NOT EXISTS OR WRONG ENTRY')
              
                                   #DISPLAY INFORMATION FUNCTION
def display():
     print("\t\t\t  -------------------------------------------")
     print("\t\t\t |            ACCOUNT INFORMATION            |")
     print("\t\t\t  -------------------------------------------")
     a=input('\t\t\t\t   USERNAME: ')
     b=input('\t\t\t\t   PASSWORD: ')
     try:
          s1="select user_name from user_accounts where password='{}'".format(b)
          c1="select fname,lname from user_accounts where password='{}'".format(b)
          cursor.execute(c1)
          data1=cursor.fetchall()[0]
          data1=list(data1)
          data1=data1[0]+''+data1[1]
          cursor.execute(s1)
          data=cursor.fetchall()[0]
          data=list(data)
          if data[0]==a:
               x=['FIRST NAME','LAST NAME','PHONE NUMBER','GENDER','DATE OF BIRTH','AGE']
               s1="select fname,lname,phno,gender,dob,age from user_accounts where password='{}'".format(b)
               cursor.execute(s1)
               data=cursor.fetchall()[0]
               data=list(data)
               print('\n\t\t\t\t\t  ACCOUNT INFORMATION')
               print('\t\t\t\t\t  -------------------\n')
               print('\t\t\t\t\t |',x[0],'-->',data[0])
               print('\t\t\t\t\t |',x[1],'-->',data[1])
               print('\t\t\t\t\t |',x[2],'-->',data[2])
               print('\t\t\t\t\t |',x[3],'-->',data[3])
               print('\t\t\t\t\t |',x[4],'-->',data[4])
               print('\t\t\t\t\t |',x[5],'-->',data[5])
          else:
               return False  
     except:
          print('ACCOUNT DOES NOT EXISTS')

                                   #MAIN FUNCTION
def main():
     while True:
          print('\t\t    --------------------------------------------------------')
          print("\t\t\t\t     1.TICKET BOOKING")
          print("\t\t\t\t     2.TICKET CHECKING")
          print("\t\t\t\t     3.TICKET CANCELLING")
          print("\t\t\t\t     4.ACCOUNT DETAILS")
          print("\t\t\t\t     5.LOG OUT")
          print('\t\t    --------------------------------------------------------')
          ch=int(input('\t\t\t\tENTER YOUR CHOICE: '))
          if ch==1:
              os.system('cls')
              ticket_book()
          elif ch==2:
              os.system('cls')
              ticket_check()
          elif ch==3:
              os.system('cls')
              ticket_cancel()
          elif ch==4:
              os.system('cls')
              display()
          elif ch==5:
              os.system('cls')
              print("THANK YOU")
              break
          else:
              print('ERROR 404: PAGE NOT FOUND')     


import mysql.connector
mycon=mysql.connector.connect(host='localhost', user='root',password='root')
cursor=mycon.cursor()
mycon.autocommit=True

s1="create database if not exists railway"
cursor.execute(s1)
s1="use railway"
cursor.execute(s1)
s1="create table if not exists railway(name varchar(100),\
    phno varchar(15) primary key, age int(4),gender varchar(50),\
        from_f varchar(100),to_t varchar(100),date_d varchar(20))"
cursor.execute(s1)
s1="create table if not exists user_accounts(fname varchar(100),\
    lname varchar(100),user_name varchar(100),\
        password varchar(100) primary key,\
            phno varchar(15),gender varchar(50),dob varchar(50),age varchar(4))"
cursor.execute(s1)

print("\t   -------------------------------------------------------------------------")
while True:
    print("\t\t\t  -------------------------------------------")
    print("\t\t\t | WELCOME TO THE RAILWAY RESERVATION SYSTEM |")
    print("\t\t\t  -------------------------------------------")
    print("\t\t\t\t\t  1.SIGN IN")
    print("\t\t\t\t\t  2.SIGN UP")
    print("\t\t\t\t\t  3.EXIT")
    print("\t   --------------------------------------------------------------------------")
    print('\t   --------------------------------------------------------------------------')

    ch=int(input("\t\t\t\t     ENTER YOUR CHOICE: "))
    if ch==1:
        signin()
    elif ch==2:
        signup()
    elif ch==3:
        print("\t\t   --------------------------------------------------------------")        
        print("\t\t\t\t\t   THANK YOU")
        print("\t\t   --------------------------------------------------------------")
        break
    else:
         print('ERROR 404: PAGE NOT FOUND')


