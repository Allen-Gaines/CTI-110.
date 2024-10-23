#Allen GAines
#10/23/24
#P3H2
#make a pay sheet

Employee_name= input("enter employee's name: ")
Hours= float(input( "enter hours worked: "))
rate= float(input ( " enter employees pay rate "))
print("--*18")
print(" Hours worked")
pay_rate= 40*rate 
if Hours > 40:
      overtime= Hours-40
      print(overtime)
      overtime_pay_rate= ( rate *1.5)
      OT_pay = overtime_pay_rate * overtime 
      
else: "has no overtime"

hours_worked= Hours
overtime = 0 
print (f" {overtime},{overtime_pay_rate},{ OT_pay },")
       
print(F"Employee's name: {Employee_name}")

#print(" Hours worked 
#if hours > 40:
      #print 
       
