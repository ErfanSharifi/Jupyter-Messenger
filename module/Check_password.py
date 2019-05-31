#!/usr/bin/python

class Check_Password():

    def __init__(self):
        pass

    def Paswd_CHecking(self, password):
        form = ["1","2","3","4","5","6","7","8","9",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'u', 'v','w', 'x', 'y', 'z',"!","@","#","$","%","^","&","*","(",")","-","+","=","{","}","[","]","<",">"]
        val= True

        if (len(password) >= 8):
            if (type(password) == str):
                for j in range(len(password)):
                    for i in range(len(form)):
                        if (password[j] == form[i]):
                            val = True
                            break
                        else:
                            val =False
            else:
                val =False
        else:
            val = False

        return val

#def main():
    
    #password =raw_input("""    *)Password must be least 8 character.
    #*)Password must be include sign and number.
    #Paswword:""")

    #print ("Please Confirm:")
    #conf =raw_input("Confirm:")





    #obj = Check_Password()
    #if (conf == password):
    #    if (obj.Paswd_CHecking(password)):
    #        print "Passowrd Format is OK"
    #    else:
    #        print "Password format is not OK"
    #else:
    #    print ("Not Same")
#main()