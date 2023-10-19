

from decimal import *
import time


x = time.clock()
def lrac2():

        nterms = int(input("Approximation de la racine carré de 5"))
        a = int(input("Nombre de chiffre significatif:"))

        count = 0
        n1 = '9/4'

        getcontext().prec = a
        

       
        
        
        if nterms <= 0:   
                print("Rentrez un nombre positif!")

        elif nterms == 1:
                print("rang 1:",nterms,":")
                print(n1)


        else:
                
                
                while count < nterms:

                        ##print("bonjour")                        
                        
                        getcontext().prec = a

                        if (count < 1):
                                ##print("n1: ",n1)
                                n2 = n1[::-1]
                                ##print("n2: ",n2)

                        if (count >= 1):
                                ##print("n1: ",n1)
                                n2 = "2/(n3 +5*n4)"
                                ##print("n2: ",n2)

                                

                        n3 = Decimal(eval((n1)))
                        ##print("n3: ",n3)
                        n4 = Decimal(eval((n2)))
                        ##print("n4: ",n4)
                        n5= (n3+5*n4)/2
                        ##print("n5: ",n5)
                        
                        n1 = "(n3+5*n4)/2"
                        
                       
                        count = count+1
                        
                        
        ##print("rang: ",count,":",n5)
        return n5
        
z = lrac2()
print(Decimal((1+z)/2))
print("temps mis: ",time.clock()-x)








       




