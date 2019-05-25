import socket
import sys
import os
import time
from tkinter import *
import sqlite3
import string
import os
import module.CheckName as chknam
import module.check_mail as chkmail
import module.Check_Mobile as chkmob


class MS_login():
 
    def __init__(self,root):

        self.root = root

        self.login_frame = Frame(root, height= 220, width =770)
        self.login_frame.grid(row =0, column =0, sticky =N+S+W+E)
        self.login_frame.grid_propagate(False)


        self.lbl_username = Label(self.login_frame, text ="Username:")
        self.lbl_username.grid(row =0, column =0,pady =30)
        self.lbl_username.grid_propagate(False)

        self.lbl_password = Label(self.login_frame,text ="Password:")
        self.lbl_password.grid(row =1, column = 0,pady =30)
        self.lbl_password.grid_propagate(False)

        self.txt_username =Entry(self.login_frame, width =50)
        self.txt_username.grid(row =0, column =1)
        self.txt_username.grid_propagate(False)

        self.txt_password =Entry(self.login_frame, width =50)
        self.txt_password.config(show ="*")
        self.txt_password.grid(row =1, column =1)
        self.txt_password.grid_propagate(False)

        self.signin_btn =Button(self.login_frame, height =2, width =9, text= "Sign-in")
        self.signin_btn.grid(row =2, column =0, padx =50, sticky =N+S+E)
        self.signin_btn.grid_propagate(False)

        self.signup_btn =Button(self.login_frame, height =2, width =9, text= "Sign-up", command =self.Sign_UP)
        self.signup_btn.grid(row =2, column =2,padx = 20,sticky =N+S+E)
        self.signup_btn.grid_propagate(False)

        Fingerprint_image =PhotoImage(file ="/root/Desktop/Messenger/Doc/finger3.png").subsample(3, 3)
        Fingerprint_image.image =Fingerprint_image
        
        self.Finger_btn =Button(self.login_frame,image =Fingerprint_image, height =45, width =90)
        self.Finger_btn.grid(row =2, column =1,padx =40, sticky =N+S+W+E)
        self.Finger_btn.grid_propagate(False)


    def Sign_UP(self):
    
        self.signup =Toplevel()
        self.signup.resizable(0,0)
        self.signup.title("Register Page")
        self.signup.geometry("1400x650+150+150")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Label \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        self.lbl_name = Label(self.signup, text ="Name:")
        self.lbl_name.grid(row =0, column =0, padx =30, pady =30)
        self.lbl_name.grid_propagate(False)

        self.lbl_Family = Label(self.signup, text ="Family:")
        self.lbl_Family.grid(row =0, column =2, padx =30, pady =30)
        self.lbl_Family.grid_propagate(False)

        self.lbl_Age = Label(self.signup, text ="Age:")
        self.lbl_Age.grid(row =1, column =0, padx =30, pady =30)
        self.lbl_Age.grid_propagate(False)

        self.lbl_mail = Label(self.signup, text ="E-mail:")
        self.lbl_mail.grid(row =1, column =2, padx =100, pady =30)
        self.lbl_mail.grid_propagate(False)

        self.lbl_Mobile = Label(self.signup, text ="Mobile:")
        self.lbl_Mobile.grid(row =2, column =0, padx =30, pady =30)
        self.lbl_Mobile.grid_propagate(False)

        self.lbl_Address = Label(self.signup, text ="Address:")
        self.lbl_Address.grid(row =2, column =2, padx =30, pady =30)
        self.lbl_Address.grid_propagate(False)

        self.lbl_username = Label(self.signup, text ="Username:")
        self.lbl_username.grid(row =3, column =0, padx =100, pady =30)
        self.lbl_username.grid_propagate(False)

        self.lbl_Password = Label(self.signup, text ="Password:")
        self.lbl_Password.grid(row =4, column =0, padx =100, pady =30)
        self.lbl_Password.grid_propagate(False)

        self.lbl_conf_Password = Label(self.signup, text ="Confirm Password:")
        self.lbl_conf_Password.grid(row =4, column =2, padx =100, pady =30)
        self.lbl_conf_Password.grid_propagate(False)

        self.lbl_Favoriate = Label(self.signup, text ="Favoriate:")
        self.lbl_Favoriate.grid(row =5, column =0, padx =100, pady =30)
        self.lbl_Favoriate.grid_propagate(False)


#///////////////////////////////////////////// text ////////////////////////////////////

        self.txt_name =Entry(self.signup, width =40)
        self.txt_name.grid(row =0, column =1)
        self.txt_name.grid_propagate(False)

        self.txt_family =Entry(self.signup, width =40)
        self.txt_family.grid(row =0, column =3)
        self.txt_family.grid_propagate(False)

        self.txt_mail =Entry(self.signup, width =40)
        self.txt_mail.grid(row =1, column =3)
        self.txt_mail.grid_propagate(False)

        self.txt_mobile =Entry(self.signup, width =40)
        self.txt_mobile.grid(row =2, column =1)
        self.txt_mobile.grid_propagate(False)

        self.txt_address =Entry(self.signup, width =40)
        self.txt_address.grid(row =2, column =3)
        self.txt_address.grid_propagate(False)

        self.txt_username =Entry(self.signup, width =40)
        self.txt_username.grid(row =3, column =1)
        self.txt_username.grid_propagate(False)

        self.txt_password =Entry(self.signup, width =40)
        self.txt_password.config(show ="*")
        self.txt_password.grid(row =4, column =1)
        self.txt_password.grid_propagate(False)

        self.txt_conf_pass =Entry(self.signup, width =40)
        self.txt_conf_pass.config(show ="*")
        self.txt_conf_pass.grid(row =4, column =3)
        self.txt_conf_pass.grid_propagate(False)

        self.txt_term =Text(self.signup,height =2, width =50)
        tar ="when you can read this statement you cn Know me."
        self.txt_term.grid(row =6, column =2)
        self.txt_term.grid_propagate(False)
        self.txt_term.insert("1.0", tar)
        self.txt_term.config(state = DISABLED)

        self.txt_Error_show =Text(self.signup,height = 7, width =40)
        self.txt_Error_show.grid(row =7, column =2)
        self.txt_Error_show.grid_propagate(False)


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Check-button \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        self.sport =BooleanVar()
        self.chk_sp =Checkbutton(self.signup, text ="Sport", variable =self.sport, onvalue ="1", offvalue ="0")
        self.chk_sp.grid(row =5, column = 1)

        self.movie =BooleanVar()
        self.chk_mv =Checkbutton(self.signup, text ="Movie", variable =self.movie, onvalue ="1", offvalue ="0")
        self.chk_mv.grid(row =5, column = 2)

        self.internet =BooleanVar()
        self.chk_int =Checkbutton(self.signup, text ="Internet", variable =self.internet, onvalue ="1", offvalue ="0")
        self.chk_int.grid(row =5, column = 3)

        self.term =BooleanVar()
        self.chk_term =Checkbutton(self.signup, text ="Do you accept Terms?",variable =self.term, onvalue ="1", offvalue ="0" )
        self.chk_term.grid(row =6, column = 1)
        

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Spinbox-Age \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        self.age =IntVar()
        self.age_sp =Spinbox(self.signup, from_ =20, to = 90, textvariable =self.age, width =5)
        self.age_sp.grid(row =1, column =1)  

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ button \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\     

        self.register_btn =Button(self.signup, text ="Register", command = self.Database)
        self.register_btn.grid(row =7, column =0, sticky = S+N+E+W, padx =50, pady =50)

        self.Clear_btn =Button(self.signup, text ="Clear", command =self.Clear)
        self.Clear_btn.grid(row =7, column =1, sticky = S+N+E+W ,padx= 50, pady =50)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Data Base \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ 

        
    def Database(self):
        database = ("/root/Documents/Messenger-DB/Messenger.db.sqlite")
        con =sqlite3.connect(database)
        cur =con.cursor()
        cur.execute("select id from document_tb")
        rows =cur.fetchall()
        if (rows == []):
                rows.append(1)
                rows =str(rows)
                rows =string.replace(rows,"[","")
                rows =string.replace(rows,"]","")
                x =int(rows)
                esme =self.txt_name.get()
                famil =self.txt_family.get()
                obj =chknam.chech_string()
                check =obj.chk_str(esme)
                gol =obj.chk_str(famil)
                if (check and gol == True):

                        sen =self.age_sp.get()
                        sen =int(sen)
                        mail =self.txt_mail.get()
                        obj =chkmail.Mail()
                        if (obj.Check_mail(mail)):
                                mobil =self.txt_mobile.get()
                                
                                obj =chkmob.Chek_mob()
                                if (obj.number_check(mobil)):
                                        addr = self.txt_address.get()
                                        mobil =int(mobil)
                                        database = ("/root/Documents/Messenger-DB/Messenger.db.sqlite")
                                        con =sqlite3.connect(database)
                                        cur =con.cursor()
                                        query =("INSERT INTO document_tb (id, name, family, age, email, mobile, address) VALUES({0:d}, '{1:s}', '{2:s}', {3:d}, '{4:s}', {5:d}, '{6:s}')".format(x, esme, famil, sen, mail, mobil, addr))
                                        cur.execute(query)
                                        con.commit()
                                else:
                                        print "Check mobile number..."
                        else:
                                print "Invalid E-mail..."
                else:
                        print "Check your input..."
        else:   
                x =rows[-1]
                x =str(x)
                x =string.replace(x,"(","")
                x =string.replace(x,")","")
                x =string.replace(x,",","")  
                x =int(x)
                x =x+1
                esme =self.txt_name.get()
                famil =self.txt_family.get()
                obj =chknam.chech_string()
                check =obj.chk_str(esme)
                gol =obj.chk_str(famil)
                if (check and gol == True):

                        sen =self.age_sp.get()
                        sen =int(sen)
                        mail =self.txt_mail.get()
                        obj =chkmail.Mail()
                        if (obj.Check_mail(mail)):
                                mobil =self.txt_mobile.get()
                                obj =chkmob.Chek_mob()
                                if (obj.number_check(mobil)):
                                        addr = self.txt_address.get()
                                        mobil =int(mobil)
                                        database = ("/root/Documents/Messenger-DB/Messenger.db.sqlite")
                                        con =sqlite3.connect(database)
                                        cur =con.cursor()
                                        query =("INSERT INTO document_tb (id, name, family, age, email, mobile, address) VALUES({0:d}, '{1:s}', '{2:s}', {3:d}, '{4:s}', {5:d}, '{6:s}')".format(x, esme, famil, sen, mail, mobil, addr))
                                        cur.execute(query)
                                        con.commit()
                                else:
                                        print "Check mobile number..."

                        else:
                                print "Invalid E-mail..."

                else:
                        print "Check your input..."



    def Clear(self):
        self.txt_name.delete("0",END)
        self.txt_family.delete("0", END)
        self.txt_address.delete("0", END)
        self.txt_mail.delete("0", END)
        self.txt_conf_pass.delete("0", END)
        self.txt_mobile.delete("0", END)
        self.txt_password.delete("0", END)
        self.txt_username.delete("0", END)

        self.age_sp.delete(0, END)
        self.chk_int.deselect()
        self.chk_mv.deselect()
        self.chk_sp.deselect()
        self.chk_term.deselect()




def main():

    root =Tk()
    root.resizable(0,0)
    root.title("Login Page")
    root.geometry("770x220+450+360")
    app =MS_login(root)
    root =mainloop()
main()