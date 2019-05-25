#!/usr/bin/python

class Chek_mob():

    def __init__(self):
        pass

    def number_check(self, mobile):

        MCI =['0910', '0911', '0912', '0913', '0914', '0915', '0916', '0917','0918','0919', '0936','0935','0930','0902', '0901', '0933', '0937', '0938', '0939']    
        b = mobile[0:4]
        b =str(b)

        val =False

        try:
            if (len(mobile)==11):
                for i in range(len(MCI)):
                    if (MCI[i] == b):
                        mobile =int(mobile)
                        val = True
                        break     
                    else:   
                        val = False 
            else:
                val =False

            return val
        except ValueError:
            pass


###def main():

#    mobile =raw_input("Please enter your mobile number:")
#    obj =Chek_mob()
#    if (obj.number_check(mobile)):
#        print ("Number is valid")
#    else:
#        print ("Number is not valid")
#main()
