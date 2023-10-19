from decimal import *
import time


def FractionOr():

        nterms = int(input("Approximation du nombre d'or avec la suite infernale de fraction avec des 1:"))
        a = int(input("Nombre de chiffre significatif:"))



        count = 0
        count2= 0
        resultat=""

        x = time.clock()
        
        if nterms <= 0:   
                print("Rentrez un nombre positif!")

        elif nterms == 1:
                print("rang 1:",nterm,":")
                print(n1)


        else:
      
                while count < nterms:
                        
                  
                        getcontext().prec = a

                        resultat=resultat+"1/(1+"
                        
                        count += 1

                resultat=resultat[:-1]

                while count2 < nterms:

                        resultat=resultat+")"
                        count2 = count2 + 1

                        
                

                
                
               

               
                   
                print("rang: ",count,":",Decimal(eval(resultat)))
                print("temps mis: ",time.clock()-x)









       


