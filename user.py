import mysql.connector
from stringHandler import handler
from tkinter import messagebox
from datetime import datetime
class Korisnik():
    def __init__(self, accid):
        global mydb
        global mycursor
        mydb=mysql.connector.connect(host="localhost",user="root",password="")
        mycursor=mydb.cursor()
        mycursor.execute("create database if not exists databaza")
        mycursor.execute("use databaza")
        mycursor.execute('select * from bank where accid = ' + accid )
        self.accid = accid
        result = mycursor.fetchall()
        result = list(result[0])
        print(result)
        print(result[1])
        print(result[1].decode(encoding='UTF-8',errors='strict'))
        print(type(result))
        name=handler(result[1])
        password=handler(result[2])
        balance=handler(result[3])
        self.name = name
        self.password = password
        self.balance = balance

    def withdraw(self, amount):
        global mycursor
        if(int(float(self.balance)) < int(amount)):
            
            messagebox.showinfo('TRANSACTION','Failed!')
            return(0)

        self.balance = int(float(self.balance)) - int(amount)
                 
        mycursor.execute(f"update bank set balance ={self.balance} where accid = {self.accid} ")
        messagebox.showinfo('TRANSAKCIJA','Uspesno ste izvrsili transakciju!')


    def deposit(self, amount):
        global mycursor
        self.balance = int(float(self.balance)) + int(amount)
                 
        mycursor.execute(f"update bank set balance ={self.balance} where accid = {self.accid} ")
        messagebox.showinfo('TRANSAKCIJA','Uspesno ste izvrsili transakciju!')

    def getInfo(self):
        return(self.accid, self.name, self.password)

    def getBalance(self):
        return self.balance

    def checkIfExists(accid):
        mydb=mysql.connector.connect(host="localhost",user="root",password="")
        mycursor=mydb.cursor()
        mycursor.execute("create database if not exists databaza")
        mycursor.execute("use databaza")
        mycursor.execute('select * from bank where accid = ' + accid )
        row = mycursor.fetchone()
        if row == None:
            return 0
        else:
            return 1 
    def addUserToDB(accid, password, name):
        mydb=mysql.connector.connect(host="localhost",user="root",password="")
        mycursor=mydb.cursor()
        mycursor.execute("create database if not exists databaza")
        mycursor.execute("use databaza")
        mycursor.execute("insert into bank values('"+accid+"','"+name+"','"+password+"','0')")
        mydb.commit()
    def PrintInfo(self):
        now = datetime.now()
        today = datetime.today()
        d1 = today.strftime("%d/%m/%Y")
        current_time = now.strftime("%H:%M:%S")
        temp = current_time
        current_time = "".join([x for x in current_time.split(":")]) #List compehension
        f= open(f"atm_{current_time}.txt","w+")
        f.write("Ime:" + self.name+"\n")
        f.write("Br.kartice:" + self.accid+"\n")
        f.write("Stanje racuna:" + str(self.balance)+"RSD"+"\n")
        f.write("Vreme:" + temp+"\n")
        f.write("Datum:" + d1+"\n")
        messagebox.showinfo('STAMPANJE','Uspesno ste izvrsili stampanje izvestaja!')
def main():
    user = Korisnik("38757")
    user.PrintInfo()


if __name__=="__main__":
    main()

    