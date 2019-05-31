#!/usr/bin/python

class Check_username():

    def __init__(self):
        pass
    
    def chk_username(self,a):

        val =False
        listt =["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-" ,"+" ,"=" ,"{" , "}", "[", "]", "<", ">"]
        for i in range(len(listt)):
            search =a.find("!")
            if (search != -1):
                val = False
            else:
                val =True
        return val
