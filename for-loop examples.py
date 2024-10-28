#for- loop examples

'''
#for loop in range 1 perameter 
for item in range(5):
    print(item)


#for loop in range 2 perameter 
for item in range(3, 10):
    print(item)

##for loop in range 3 perameter 
for item in range(2,21,2):
    print(item)




trees=[ "pine " , "dogwood", "palm" , "oak"]

for tree in trees:
    print (tree, "tree")
    print("**********")



num_list = [ 0, -7 ,2, 8]
num_sum = 0

for num in num_list:
    #num_sum+= num
    num_sum= num_sum +num
    
print (num_sum)
'''

# while loop  examples

UserChoice = input( " wanna run the program?")
while UserChoice == "yes":
    print ("^:^"* 10)
    print ("program is running")
    print()
    UserChoice= input("run again?")

print(" thanks for using the program") 
    
           
