MCI =['0910', '0911', '0912', '0913', '0914', '0915', '0916', '0917','0918','0919', '0936','0935','0930','0902', '0901', '0933', '0937', '0938', '0939']    

q =raw_input("Please insert:")
val =False
for i in range(len(MCI)):
    if (MCI[i] == q):
        val = True
        break
    else:
            val =False
            
            

print val


