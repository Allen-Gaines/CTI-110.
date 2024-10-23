#Allen Gaines
#10/14/2024
#p3lab
#calculate the most efficiant change as coins
'''
#regular division
print (100/3)
#floor division - returns the integer portion
print (100//3)

#modulo- gives only the remainder

print(100%3)
print(7%4)
``
'''

money = float(input("Enter the amount of money as a float: $"))

# convert money as a whole number

money= round(money * 100)

#money= int(money * 100) may need to round this value money= round(money*100) 
#print(money)
#get whole dollars for money ammount 
Dollars = money//100
#print(f"Dollars: {Dollars}")
#print(Dollars)
# remove dollar ammount from money
money= money - (Dollars * 100)
if money == 0:
    print("no change")
#print(money)
Dollars = money//100
print(f"Dollars: {Dollars}")
#get quarters
Quarters = money // 25
print (f" Quarters: {Quarters}")
money= money - (Quarters * 25)
dimes= money //10
print (f" dimes: {dimes}")
money= money - (dimes * 10)

nickels= money//5
print (f' nickels: {nickels}')
money= money - (nickels * 5)
    

pennies= money
print(f"pennies: {pennies}")

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
