#!/usr/bin/python

class chech_string():


    def __init__(self):
        pass
        
    def chk_str(self,a):
        
        val =False

        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'u', 'v','w', 'x', 'y', 'z']

        if (type(a) == str):
            for i in range(len(a)):
                for j in range(len(alphabet)):
                    if (a[i]== alphabet[j]):
                        val =True
                        break
                    else:
                        try:
                            f =int(a[i])
                            val =False
                        except ValueError:
                            pass

        else:
            val =False

        return val


