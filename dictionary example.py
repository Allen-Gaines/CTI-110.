# in class example using dictionary

#create a dictionary using a key : value pairs

person1={"name":input("enter name: "), "age":25, "height":50.25}

#get info back out from dictionary using the key

print(person1["height"])

#print the enitire dictionary
print(person1)
print("\n\n")
#add key value pair to dictionary

person1["dob"] = "10-20-1990"
print(person1)

person1.update({"hair color":"brown"})
print("\n\n")

print(person1)

#remove a key value
del person1["height"]

print("\n\n")
print(person1)

#create key value :value pair from user input

person1["height"] = input(f"enter height of {person1['name']}: ")
print()
print(person1)
print("\n\n\n")

#print to screen and ask for what value do they want
print(person1.keys(), "\n")
UserChoice = input(f" what would you like to know about {person1['name']}? ")
print()
print(person1[UserChoice])

       



