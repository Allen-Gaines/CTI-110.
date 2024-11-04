#Allen GAines
#11/4/2024
#p4hw1
# Using while statement to get grADED OUTPUTS 





Num_score= int(input("How many scores do you want to enter "))
Score_list=[] 
for scores in range(0, Num_score):
    User_input = float(input(f"Enter score #{scores +1}"))
    while User_input <0 or User_input >100:
        print(" INVALID SCORE ENTERED!!!")
        print ("score should be between 0 and 100")
        User_input = float(input(f"Enter score #{scores +1} again"))
        
    Score_list.append(User_input)

print()
print()
print("----------------Results-----------------")
Average = sum(Score_list)/len(Score_list)
if  Average>=90:
    f_grade= "A"
elif Average < 89 and Average >79:
    f_grade="B"
elif Average < 79 and Average > 69:
    f_grade= "C"
elif Average < 69 and Average > 59:
    f_grade = "D"
else:
    f_grade = "F"

lowest_grade = min(Score_list)
Score_list.remove(lowest_grade)

print(f"{'Lowest Grade:':<15} {lowest_grade:}")
print(f"{'Modified list:':<15} {Score_list:}")
print(f"{'Average:':<15} {Average:.2f}")
print (f"{'Grade:':<15} {f_grade:}")
print("----"*18)


    
