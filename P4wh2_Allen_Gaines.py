#Allen Gaines



UserInput= input('enter employee name or "done" to terminate: ') 

employee_Ammout=0
total_OT=0
totalHours=0

grosspay=0
while UserInput != "done":
    employee_Ammout +=1
    Hours= float(input( f"enter hours {UserInput} worked: "))
    totalHours += Hours
    rate= float(input ( f" enter {UserInput} pay rate " ))
    print()
    pay_rate= 40*rate
    

    if Hours > 40:
          overtime= Hours-40
          total_OT +=overtime 
          print(overtime)
          overtime_pay_rate= ( rate *1.5)
          OT_pay = overtime_pay_rate * overtime 
          fullpay= OT_pay+pay_rate
          grosspay += fullpay 
    else:
        hours_worked= Hours
        overtime = 0
        OT_pay = 0
        fullpay= OT_pay+pay_rate
        grosspay += fullpay 
    print(f"Employee's name: {UserInput}")
   
    

    print(f" Hours worked,     pay rate,     overtime,     overtime pay,     reghours pay,  gross pay")

    print( f" {Hours:<15}{rate:<15}{overtime:<15}{OT_pay:<15}${pay_rate:<15}${fullpay:<15}")

    UserInput= input('enter employee name or "done" to terminate: ') 
    
print(f" total number of employees entered: {employee_Ammout} ")
print (f"total ammout paid overtime: {total_OT}  ")
print (f"total ammount of regular hours: {totalHours} ")
print (f"total ammount paid in gross: ${grosspay} " ) 
    
