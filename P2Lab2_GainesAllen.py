# Allen Gaines
# 10/2/2024
#P2Lab2
# use a dictionary to retrieve and store data

#creates the dictionary 
Cars = {"Camaro":18.21, "Prius":52.36, "Model_S":110, "Silverado":26}
#print all keys 
print(Cars.keys())
print()
#get the car from user 
usercar=input("Enter a vehicle to see its mpg: ")
print()
#print mpg from user car 
print(f"The {usercar} gets {Cars[usercar]} mpg.")
print()
#get miles drive
Miles=float(input(f"how many miles will you drive the {usercar}? "))
print()
#calculate mpg
Mpg= Miles/Cars[usercar]
print(f"{Mpg:.2f} gallon(s) of gas are needed to drive the {usercar} {Miles} miles.")
