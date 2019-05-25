#!/usr/bin/python

class Mail():

    def __init__(self):
        pass

    def Check_mail(self,mail):

        val = False
        status =False

        company =['gmail.com', 'yahoo.com', 'msn.com', 'hotmail.com']
        if (type(mail) == str):
            if mail.find("@"):
                a =mail.split("@")
                b = str(a[1])
                for i in range(len(company)):
                    if (b == company[i]):
                        val = True
                        break
                    else:
                        status =True

        else:
            val =False
        return val


#if __name__ == "__main__":

#    mail =raw_input("Please Enter Your mail:")
#    obj =Mail()
#    if (obj.Check_mail(mail)):
#        print ("Valid Value")
#    else:
#        print ("Invalid Value")