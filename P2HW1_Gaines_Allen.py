
#Allen Gaines
#10/7/2024
#P2HW1
#creating a way for user to calculate a buget for a trip and formatting an f string.
print("This program calculates and displays travel expenses")
print()
#get the input of each part of the buget 
Budget=int(input("Enter budget"))
print()#creating spaces
travel=input("Enter your travel destination: " )
print()
gas= int(input("How much do you think you will spend on gas? "))
print()
hotel=int(input ("Approximately, how much will you need for accomendation/hotel? "))
print()
food= int(input(f"Last, how much do you need for food? "))
print("------------Travel Expenses------------")
#formatting f strings 
print(f"{'Location:':<18}{travel:<30}")
print (f"{'Initial Budget:':<18}${Budget:<30}")
print(f"{'Fuel:':<18}${gas:<30}")
print(f"{'Accomodation:':<18}${hotel:<30}")
print(f"{'Food:':<18}${food:<30}")
print("-" * 40)
#calculation for output
remaining= Budget- gas - hotel-food
250
print()
print("Remaining balence:","$",remaining) 


