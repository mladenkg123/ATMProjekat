################## IMPORTOVANE BIBLIOTEKE #################################
from tkinter import *
from tkinter import messagebox
import  tkinter.messagebox
from tkinter import BOTH, END, LEFT
import tkinter as tk
import os
from PIL import Image,ImageTk
import time
import random
import mysql.connector
from user import Korisnik
os.chdir("C:\\Users\\Mladen\\Desktop\\atmprojekat\\images")

################## TRENUTNO STANJE  #################################

current_balance=0.00
global korisnik

class Bankomat(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
    

        self.shared_data={'Balance':tk.IntVar()}

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        ################## INICIJALIZACIJA STRANICA U KONTEJNER #################################
        for F in (StartPage, MenuPage, WithdrawPage,DepositPage,BalancePage,InfoPage):
            page_name = F.__name__
            print(page_name)
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")
        
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

############################ START STRANICA #############################
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#495057')
        self.controller = controller
        self.controller.title('Projekat Bankomat')
        self.controller.state('zoomed')
        self.controller.iconphoto(False,tk.PhotoImage(file='atm-machine.png'))

        heading=tk.Label(self,text='Bankomat Projekat',font=('Arial',45,'bold'),foreground='white',background='#495057')
        heading.pack(pady=25)

        space_label=tk.Label(self,height=4,bg='#495057').pack()

        password_label=tk.Label(self,text=(f'Dobrodosao {user_display_name} u Nas Bankomat'),font=('BatmanForeverAlternate',17),bg='#3d3d5c',fg='white').pack(pady=10)

        def next_page():
            controller.show_frame('MenuPage')

        entry_button = tk.Button(self,text='Ulaz',font=('Arial',12),command=next_page,relief='raised',borderwidth=3,width=23,height=3).pack(pady=10)

        def Quit():
            self.controller.destroy()

        def popup():
            response=messagebox.askyesno('Izlaz','Da li zelite da izadjete?')

            if response == 1:
                return Quit()
            else:
                return

        quit1 = tk.Button(self,text='Izlaz',font=('Arial',12),command=popup,relief='raised',borderwidth=3,width=23,height=3).pack(pady=10)


        dualtone_label=tk.Label(self, text='',font=('Arial',13),fg='white',bg='#343A40',anchor='n')
        dualtone_label.pack(fill='both',expand='True')

        def changescreen():
            self.controller.destroy()
            main_screen()

        def popup2():
            response=messagebox.askyesno('Izlaz','Da li zelite da koristite drugi nalog?')

            if response == 1:
                return changescreen()
            else:
                return

        register_login_screen = tk.Button(dualtone_label,text='Promena naloga',font=('Arial',12),command=popup2,relief='raised',borderwidth=3,width=23,height=3).pack(pady=10,padx=10,side='bottom',anchor='e')

        ################## BOTTOM FRAME ############################
        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3).pack(fill='x',side='bottom')

        visa_photo= tk.PhotoImage(file='visa.png')
        visa_label=tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image=visa_photo

        mastercard_photo= tk.PhotoImage(file='mastercard.png')
        mastercard_label=tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image=mastercard_photo

        american_express_photo= tk.PhotoImage(file='american_express.png')
        american_express_label=tk.Label(bottom_frame,image=american_express_photo)
        american_express_label.pack(side='left')
        american_express_label.image=american_express_photo

        def tick():
            current_time=time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200,tick)


        time_label=tk.Label(bottom_frame,font=('Arial',12))
        time_label.pack(side='right')
        tick()

        credits=tk.Label(bottom_frame,text='Projekat iz Softverskog inzenjeringa Mladen Cvetkovic 649-2019',font=('Arial',15)).pack()



################## MENI  ###########################
class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#495057')
        self.controller = controller
        heading=tk.Label(self,text='MENI',font=('Arial',45,'bold'),foreground='white',background='#495057')
        heading.pack(pady=25)
        main_menu_label=tk.Label(self,text='Glavni Meni',font=('Arial',13),fg='white',bg='#495057')
        main_menu_label.pack(pady=5)
        slection_label=tk.Label(self,text='Izaberite uslugu',font=('Arial',13),fg='white',bg='#495057')
        slection_label.pack(fill='x',pady=5)
        button_frame=tk.Frame(self,bg='#343A40')
        button_frame.pack(fill='both',expand='True')

        def withdraw():
            controller.show_frame('WithdrawPage')

        withdraw_button=tk.Button(button_frame,text='Podigni iznos',font=('Arial',13),command=withdraw,relief='raised',borderwidth=3,width=30,height=4)
        withdraw_button.grid(row=0,column=0,pady=7)

        def deposit():
            controller.show_frame('DepositPage')

        deposit_button=tk.Button(button_frame,text='Uplati iznos',font=('Arial',13),command=deposit,relief='raised',borderwidth=3,width=30,height=4)
        deposit_button.grid(row=1,column=0,pady=5)
        def balance():
            controller.show_frame('BalancePage')

        balance_button=tk.Button(button_frame,text='Stanje racuna',font=('Arial',13),command=balance,relief='raised',borderwidth=3,width=30,height=4)
        balance_button.grid(row=0,column=1,pady=7,padx=794)
        
        def stamp():
            global korisnik
            os.chdir("C:\\Users\\Mladen\\Desktop\\atmprojekat")
            korisnik.PrintInfo()
            os.chdir("C:\\Users\\Mladen\\Desktop\\atmprojekat\\images")
        stampanje_button=tk.Button(button_frame,text='Stampanje izvestaja',font=('Arial',13),command=stamp,relief='raised',borderwidth=3,width=30,height=4)
        stampanje_button.grid(row=3,column=0,pady=7)
        
        def info():
            controller.show_frame('InfoPage')

        info_button=tk.Button(button_frame,text='Informacije o korisniku',font=('Arial',13),command=info,relief='raised',borderwidth=3,width=30,height=4)
        info_button.grid(row=2,column=0,pady=5)

        def exit():
            controller.show_frame('StartPage')


        exit_button=tk.Button(button_frame,text='Izlaz',font=('Arial',13),command=exit,relief='raised',borderwidth=3,width=30,height=4)
        exit_button.grid(row=1,column=1,pady=7)

################## WITHDRAW STRANICA #################################
class WithdrawPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#495057')
        self.controller = controller

        heading=tk.Label(self,text='databaza ATM',font=('Arial',45,'bold'),foreground='white',background='#495057')
        heading.pack(pady=25)
        choose_amount_label=tk.Label(self,text='Izaberite vrednost koju zelite da podignete!',font=('Arial',13),fg='white',bg='#495057')
        choose_amount_label.pack()
        button_frame=tk.Frame(self,bg='#343A40')
        button_frame.pack(fill='both',expand='True')

        def withdraw(amount):
            global korisnik
            global current_balance
            korisnik.withdraw(amount)  
            controller.shared_data['Balance'].set(korisnik.balance)
            controller.show_frame('MenuPage')



        sto_button=tk.Button(button_frame,text='100RSD',font=('Arial',12),command=lambda:withdraw(100),relief='raised',borderwidth=3,width=30,height=4)
        sto_button.grid(row=0,column=0,pady=5)

        dvesta_button=tk.Button(button_frame,text='200RSD',font=('Arial',12),command=lambda:withdraw(200),relief='raised',borderwidth=3,width=30,height=4)
        dvesta_button.grid(row=1,column=0,pady=5)

        petsto_button=tk.Button(button_frame,text='500RSD',font=('Arial',12),command=lambda:withdraw(500),relief='raised',borderwidth=3,width=30,height=4)
        petsto_button.grid(row=2,column=0,pady=5)

        hiljadu_button=tk.Button(button_frame,text='1000RSD',font=('Arial',12),command=lambda:withdraw(1000),relief='raised',borderwidth=3,width=30,height=4)
        hiljadu_button.grid(row=3,column=0,pady=5)

        dvehiljade_button=tk.Button(button_frame,text='2000RSD',font=('Arial',12),command=lambda:withdraw(2000),relief='raised',borderwidth=3,width=30,height=4)
        dvehiljade_button.grid(row=0,column=1,pady=5,padx=794)

        pethiljada_button=tk.Button(button_frame,text='5000RSD',font=('Arial',12),command=lambda:withdraw(5000),relief='raised',borderwidth=3,width=30,height=4)
        pethiljada_button.grid(row=1,column=1,pady=5)

        desethiljada_button=tk.Button(button_frame,text='10000RSD',font=('Arial',12),command=lambda:withdraw(10000),relief='raised',borderwidth=3,width=30,height=4)
        desethiljada_button.grid(row=2,column=1,pady=5)

        cash=tk.StringVar()
        other_amount_entry=tk.Entry(button_frame,font=('Arial',12),textvariable=cash,width=28,justify='right')
        other_amount_entry.grid(row=3,column=1,pady=4,ipady=30)

        other_amount_heading=tk.Button(button_frame,text='PODIGNI',font=('Arial',25),command=lambda:withdraw(cash.get()),borderwidth=0,relief='raised',activeforeground='white',activebackground='grey',bg='grey',fg='white')
        other_amount_heading.grid(row=4,column=1)

        def other_amount(_):
            global current_balance
            try:
                val=int(cash.get())

                if int(cash.get())>current_balance:
                    messagebox.showwarning('WARNING','Nemate dovoljno sredstava!')
                    other_amount_entry.delete(0,END)
                elif int(cash.get())<0:
                    messagebox.showwarning('WARNING','Pogresan Unos!')
                    other_amount_entry.delete(0,END)
                else:

                    current_balance -= int(cash.get())
                    controller.shared_data['Balance'].set(current_balance)
                    cash.set('')
                    messagebox.showinfo('TRANSACTION','Transakcija uspesno izvrsena!')
                    controller.show_frame('MenuPage')
                    mydb=mysql.connector.connect(host="localhost",user="root",password="")
                    mycursor=mydb.cursor()
                    mycursor.execute("use databaza")
                    mycursor.execute(f"update bank set balance ={current_balance} where accid = {username1} ")
                    mydb.commit()
            except ValueError:
                messagebox.showwarning('WARNING','Pogresan Unos!')
                cash.set('')

        other_amount_entry.bind('<Return>',other_amount)

################## DEPOSIT STRANICA #################################
class DepositPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#495057')
        self.controller = controller

        heading=tk.Label(self,text='databaza ATM',font=('Arial',45,'bold'),foreground='white',background='#495057')
        heading.pack(pady=25)

        space_label=tk.Label(self,height=4,bg='#495057').pack()

        enter_amount_label=tk.Label(self,text='Unesite vrednost koju zelite da uplatite:',font=('Arial',13),bg='#495057',fg='white').pack(pady=10)

        cash=tk.StringVar()
        deposit_entry=tk.Entry(self,textvariable=cash,font=('Arial',12),width=22)
        deposit_entry.pack(ipady=7)

        def deposit_cash(amount):
            global current_balance
            global korisnik
            korisnik.deposit(amount)
            controller.shared_data['Balance'].set(korisnik.balance)
            controller.show_frame('MenuPage')
            
            

        enter_button=tk.Button(self,text='Uplati',font=('Arial',13),command=lambda:deposit_cash(cash.get()),relief='raised',borderwidth=3,width=23,height=3)
        enter_button.pack(pady=10)

        two_tone_label=tk.Label(self,bg='#343A40')
        two_tone_label.pack(fill='both',expand=True)

################## BALANCE STRANICA #################################
class BalancePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#495057')
        self.controller = controller

        heading=tk.Label(self,text='Projekat Bankomat',font=('Arial',45,'bold'),foreground='white',background='#495057')
        heading.pack(pady=25)
        global korisnik 
        self.balance_var = tk.StringVar()
        self.balance_var.set(korisnik.balance)
        controller.shared_data['Balance'].trace('w', self.on_balance_changed)
        controller.shared_data['Balance'].set(current_balance)

        balance_label = tk.Label(self, text='Stanje racuna', font=('Arial',13),fg='white', bg='#495057', anchor='w')
        balance_label.pack()

        upperframe=tk.Frame(self,bg='#343A40')
        upperframe.pack(fill='both',expand='True')

        balance_label = tk.Label(upperframe, textvariable=self.balance_var, font=('Arial',16),fg='white', bg='#33334d', anchor='w')
        balance_label.pack(pady=7)

        button_frame=tk.Label(self,bg='#495057')
        button_frame.pack(fill='both')

        def menu():
            controller.show_frame('MenuPage')

        menu_button=tk.Button(button_frame,command=menu,text='Meni',font=('Arial',13),relief='raised',borderwidth=3,width=23,height=4)
        menu_button.pack(pady=10)

        def exit():
            controller.show_frame('StartPage')

        exit_button=tk.Button(button_frame,text='Izlaz',command=exit,font=('Arial',13),relief='raised',borderwidth=3,width=23,height=4)
        exit_button.pack(pady=5)

    def on_balance_changed(self, *args):
        self.balance_var.set('Trenutno stanje : RSD '+str(self.controller.shared_data['Balance'].get()))

class InfoPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#495057')
        self.controller = controller
        global korisnik
        heading=tk.Label(self,text='databaza ATM',font=('Arial',45,'bold'),foreground='white',background='#495057')
        heading.pack(pady=25)
        main_menu_label=tk.Label(self,text='Informacije o nalogu',font=('Arial',13),fg='white',bg='#495057')
        main_menu_label.pack(pady=5)

        upperframe=tk.Frame(self,bg='#343A40')
        upperframe.pack(fill='both',expand='True')

        button_frame=tk.Frame(self,bg='#343A40')
        button_frame.pack(fill='both')

        user_display_name = korisnik.name 
        username1 = korisnik.accid
        pass_code_read = korisnik.password
        
        name_info = tk.Label(upperframe, text=f'Ime : {user_display_name}', font=('Arial',16),fg='white', bg='#495057')
        name_info.pack(pady=5)

        accid_info = tk.Label(upperframe, text=f'Broj kartice : {username1}', font=('Arial',16),fg='white', bg='#495057')
        accid_info.pack(pady=5)

        pin_info = tk.Label(upperframe, text=f'Pin : {pass_code_read}', font=('Arial',16),fg='white', bg='#495057')
        pin_info.pack(pady=5)

        def exit():
            controller.show_frame('MenuPage')

        exit_button=tk.Button(button_frame,text='Meni',command=exit,font=('Arial',13),relief='raised',borderwidth=3,width=23,height=4)
        exit_button.pack(pady=20,padx=10)


################## CLASS DEFINE FUNKCIJA ######################
def clsdef():

        app = Bankomat()
        app.mainloop()

####### REGISTER/LOGIN #####


def password_not_recognised():
  messagebox.showwarning('WARNING',('Pogresna sifra!'))

##################ABOUT SCREEN#################################
def about():
  global screen3
  screen3 = Toplevel(screen)
  screen3.title("About")
  screen3.geometry("380x90+750+230")
  screen3.configure(bg='grey')
  screen3.iconphoto(False,tk.PhotoImage(file='atm-machine.png'))
  Label(screen3,bg='grey', text = "Projekat iz Softverskog inzenjeringa\n Student:Mladen Cvetkovic 649-2019 \n Tkinter i mqsql databaza\n",font = ("Arial", 10,'bold')).pack()

##################WARNING_SCREEN######################
def user_not_found():
  messagebox.showwarning('WARNING',('Nije pronadjen vas serijski br!'))

##################REGISTER KORISNIK###################
def register_user():
  global username_info
  username_info = str(rand)
  password_info = password.get()
  name_info     = name.get()
  if Korisnik.checkIfExists(username_info) == 0 :
    Korisnik.addUserToDB(username_info, password_info, name_info)
    screen1.destroy()
  else:
    messagebox.show("Greska!","GRESKA!")

################## LOGIN VERIFIKACIJA#################################
def login_verify():
  global current_balance
  global username1
  global user_display_name
  global korisnik
  global kID
  global user_name
  global user_pass_1
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)

  checker = Korisnik.checkIfExists(username1)


  if username1.isalpha():
        messagebox.showwarning('WARNING',('Pogresan unos!'))
        username_entry1.delete(0, END)
        password_entry1.delete(0,END)

  elif str(username1)=='':
        messagebox.showwarning('WARNING',('Nije dodeljen serijski br!'))
        password_entry1.delete(0,END)
  elif str(username1).isspace():
        messagebox.showwarning('WARNING',('Nije dodeljen serijski br!'))
        username_entry1.delete(0, END)
        password_entry1.delete(0,END)
  elif username1.isalnum():
      if username1.isdigit():
        if checker != 0:
                    korisnik = Korisnik(username1)
                    user_pass_1 = korisnik.password
                    current_balance = korisnik.balance 
                    user_name = korisnik.name
                    user_display_name = korisnik.name
                    kID = korisnik.accid
                    screen2.destroy()
                    screen.destroy()
                    clsdef()    
        elif password1 != str(user_pass_1):
                password_not_recognised()
        else:
                user_not_found()        

##################REGISTER DISPLEJ#######################
def register():
  global screen1
  global password_entry
  global username_entry
  global rand
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("380x470+750+230")
  screen1.configure(bg='grey')
  screen1.iconphoto(False,tk.PhotoImage(file='atm-machine.png'))

  photo = PhotoImage(file="RegisterSide.png")
  label = Label(screen1,image=photo,bg='grey',height="200", width="150")
  label.image = photo
  label.pack(pady=5)

  global username
  global password
  global name

  global name_entry

  username = StringVar()
  password = StringVar()
  name     = StringVar()

  Label(screen1, text = "Unesite detalje ispod kako bi ste se registrovali!",bg='grey',font = ("Arial", 10)).pack()

  Label(screen1, text = "",bg='grey').pack()
  Label(screen1, text = "Ime: ",font = ("Arial", 10),bg='grey').pack()
  name_entry = Entry(screen1,font = ("Arial",10), textvariable = name)
  name_entry.pack()

  Label(screen1, text = "Broj kartice:",font = ("Arial", 10),bg='grey').pack()
  rand=random.randint(1,100000)
  username=Label(screen1, text = rand,font = ("Arial", 11),bg='grey').pack()

  Label(screen1, text = "Pin",font = ("Arial", 10),bg='grey').pack()
  password_entry =  Entry(screen1,font = ("Arial",10), textvariable = password)
  password_entry.config(fg='black',show='●')
  password_entry.pack()

  Label(screen1, text = "",bg='grey').pack()

  img1 = PhotoImage(file="register123.png")
  photoimage1 = img1.subsample(3, 3)
  img1Btn = Button(screen1,command = register_user,image=photoimage1,bg='#635C5C',activebackground='grey',height="50", width="150",relief=FLAT)
  img1Btn.image = photoimage1
  img1Btn.pack()

##################LOGIN DISPLEJ####################
def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Login")
  screen2.geometry("380x470+750+230")
  screen2.configure(bg='grey')
  screen2.iconphoto(False,tk.PhotoImage(file='atm-machine.png'))

  photo = PhotoImage(file="LoginSide.png")
  label = Label(screen2,image=photo,bg='grey',height="200", width="150")
  label.image = photo
  label.pack(pady=5)

  Label(screen2, text = "Unesite detalje ispod kako bi ste se ulogovali!",bg='grey',font = ("Arial", 10)).pack()
  Label(screen2, text = "",bg='grey').pack()

  global username_verify
  global password_verify

  username_verify = StringVar()
  password_verify = StringVar()


  global username_entry1
  global password_entry1

  Label(screen2, text = "Broj kartice: ",bg='grey',font = ("Arial", 10)).pack()
  username_entry1 = Entry(screen2,font = ("Arial",10) ,textvariable = username_verify)
  username_entry1.pack()

  Label(screen2, text = "",bg='grey').pack()
  Label(screen2, text = "Pin",bg='grey',font = ("Arial", 10)).pack()
  password_entry1 = Entry(screen2,font = ("Arial",10), textvariable = password_verify)
  password_entry1.config(fg='black',show='●')
  password_entry1.pack()
  Label(screen2, text = "",bg='grey').pack()

  img1 = PhotoImage(file="login123.png")
  photoimage1 = img1.subsample(3, 3)
  img1Btn = Button(screen2,command = login_verify,image=photoimage1,bg='#635C5C',activebackground='grey',height="50", width="150",relief=FLAT)
  img1Btn.image = photoimage1
  img1Btn.pack()

################REGISTER/LOGIN##################
def main_screen():
  global screen
  screen = Tk()
  screen.geometry("920x760+485+100")
  screen.title("databaza")
  screen.configure(bg='grey')
  screen.iconphoto(False,tk.PhotoImage(file='atm-machine.png'))


  Label(text = "Bankomat Projekat",fg='#635C5C', bg = "black", width = "300", height = "2", font = ("Arial", 15,'bold')).pack()
  Label(text = "",bg='grey').pack()

  img = ImageTk.PhotoImage(Image.open("ATMProjekat-1.png"))
  panel = Label(screen, image = img,bg='grey', height="225", width="225")
  panel.pack(pady="30")

  photo1 = PhotoImage(file="login123.png")
  photoimage1 = photo1.subsample(2, 2)
  Button(command = login,bg='#635C5C',activebackground='grey',relief=FLAT,image = photoimage1, height="50", width="150").pack(pady=5)

  Label(text = "",bg='grey',).pack()

  photo2 = PhotoImage(file="register123.png")
  photoimage2 = photo2.subsample(2, 2)
  Button(command = register,bg='#635C5C',activebackground='grey',relief=FLAT,image = photoimage2,height="50", width="150").pack(pady=5)

  Label(text = "",bg='grey').pack()

  photo3 = PhotoImage(file="about123.png")
  photoimage3 = photo3.subsample(2, 2)
  Button(command = about,bg='#635C5C',activebackground='grey',relief=FLAT,image = photoimage3,height="50", width="150").pack(pady=5)

  screen.mainloop()

main_screen()