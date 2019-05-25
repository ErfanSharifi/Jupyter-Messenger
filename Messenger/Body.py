#!/usr/bin/python

import socket
import sys
import os
import time
from tkinter import *


class Infrastructure():
        
        def __init__(self,root):

                self.root = root

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ login-Frame \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



        

                #self.login_frame =Frame(root, height =100, width =100, background = "blue")
                #self.login_frame.grid()
                #self.login_frame.grid_propagate(False)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Frame \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

                self.left = Frame(self.root, height = 915, width = 350,background = "red")
                self.left.grid(row = 0, column =0, sticky = N+S+E+W, padx =5, pady = 5)
                self.left.grid_propagate(False)

                self.right = Frame(self.root,height = 300, width = 530,background = "green")
                self.right.grid(row = 0, column = 1, sticky = N+S+W, padx = 5, pady =5)
                self.right.grid_propagate(False)
                
                self.conn = Frame(self.left, height = 50, width = 600,background = "yellow")
                self.conn.grid(row = 0, column =0, sticky =N+S+E+W)
                self.conn.grid_propagate(False)

                self.set = Frame (self.conn, height = 50, width = 50,background = "Pink")
                self.set.grid(row =0, column =0 ,sticky =N+S+E+W)
                self.set.grid_propagate(False)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Connection-Label \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

                self.lbl_connection = Label(self.conn, text = "Network Status:")
                self.lbl_connection.grid(row = 0, column = 1,padx =5, pady =5)
                self.lbl_connection.grid_propagate(False)

                self.txt_connection = Text(self.conn, height =1, width = 13)
                self.txt_connection.grid(row = 0, column = 3, padx =5, pady = 5)
                self.txt_connection.grid_propagate(False)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Connection-check \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        
                self.ip ="www.google.com"
                self.check =os.system("ping -c 3"+ (self.ip))
                if self.check == 0:
                        #self.result = "Connected"
                        self.txt_connection.insert(END, "Connected")
                        self.txt_connection.config(state = DISABLED)
                else:
                        #self.result = "Not Connected"
                        self.txt_connection.insert(END, "Not-Connected")
                        self.txt_connection.config(state = DISABLED)


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Setting-Button \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

                Setting_image =PhotoImage(file = "/root/Desktop/Messenger/Doc/menu30.png").subsample(15, 15)
                Setting_image.image = Setting_image

                self.Setting_Button =Button(self.set, image = Setting_image, height =45,width = 45, command =self.Settings ,compound = LEFT)
                self.Setting_Button.grid(sticky =N+S+E+W)
                self.Setting_Button.place()

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\Settings-Bottun\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        

        def Settings(self):
                self.new_windows =Toplevel()
                self.new_windows.geometry("310x925+300+600")
                self.new_windows.title("Setting")
                self.new_windows.resizable(0,0)


                self.frame_in_setting =Frame(self.new_windows, height =925, width=925, background ="grey")
                self.frame_in_setting.grid(row =0, column =0, sticky =N+S+E+W)
                self.frame_in_setting.grid_propagate(False)

                self.seperat =LabelFrame(self.new_windows, text= "Profile")
                self.seperat.grid(row =0, column =0)

                








def main():

    root =Tk()
    root.resizable(0,0)
    root.geometry("900x925+300+600")
    root.title("Jupiter Messenger")
    app =Infrastructure(root)
    root.mainloop()


main()
