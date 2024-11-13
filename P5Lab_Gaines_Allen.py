#Allen Gaines
#11/3/2024
#p5lab
#simulate self checkout using funtions


#import random libraey to us

import random 


def disperse_change(money):
    print(money)
    money= int(round(money*100,2))
    
    #get whole dollars for money ammount 
    Dollars = money//100
    #print(f"Dollars: {Dollars}")
    #print(Dollars)
    # remove dollar ammount from money
    money= money - (Dollars * 100)
    if money == 0:
        print("no change")
    #print(money)
   
    #print(f"Dollars: {Dollars}")
    #get quarters
    Quarters = money // 25
    #print (f" Quarters: {Quarters}")
    money= money - (Quarters * 25)
    dimes= money //10
    #print (f" dimes: {dimes}")
    money= money - (dimes * 10)

    nickels= money//5
    #print (f' nickels: {nickels}')
    money= money - (nickels * 5)
        

    pennies= money
    #print(f"pennies: {pennies}")

    if Dollars >= 1:
        if Dollars == 1:
            print (f"{Dollars} Dollar")
        else: print(f"{Dollars} Dollars")
    if Quarters >= 1:
        if Quarters == 1:
            print (f"{Quarters} Quarter")
        else: print(f"{Quarters} Quarters")
    if dimes >= 1:
        if dimes == 1:
            print (f"{dimes} Dime")
        else: print(f"{dimes} Dims")
    if nickels >= 1:
        if nickels == 1:
            print (f"{nickels} Nickel")
        else: print(f"{nickels} Nickels")
    if pennies >= 1:
        if pennies == 1:
            print (f"{pennies} Pennie")
        else: print(f"{pennies} Pennies")
        

def main ():
    
    money= round(random.uniform(0.01, 100.00), 2)
    print(f'You owe ${money:.2f}' )
    putin= float(input("how much money did you put in the self checkout? $"))
    money= putin- money
    money= round(money,2)
    
  
    disperse_change(money)

   
 





     
        





 

   
    
  
 #call the main    
if __name__=="__main__":
    main()

   







