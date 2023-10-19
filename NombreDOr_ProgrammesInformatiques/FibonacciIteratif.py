from decimal import *
import time


def FibonacciIteratif():

        nterms = int(input("Approximation du nombre d'or avec la suite de Fibonacci au rang:"))
        a = int(input("Nombre de chiffre significatif:"))


        n1 = 0
        n2 = 1
        count = 0

        x = time.clock()
        
        if nterms <= 0:   
                print("Rentrez un nombre positif!")

        elif nterms == 1:
                print("rang 1:",nterms,":")
                print(n1)


        else:
      
                while count < nterms:
                        
                  
                        getcontext().prec = a
                        temp = n1 + n2
                  
                        n1 = n2
                        n2 = temp
                        count += 1
                        y=time.time
        print("rang: ",count,":",Decimal(n2)/Decimal(n1))
        print("temps mis: ",time.clock()-x)








       


