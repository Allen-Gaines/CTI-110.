
#Allen Gaines
#10/14/24
#PW3H1
# use branching to determin A LETTER GRADE 

#getting grades from user 
Grades = []
model_1= float(input(f"Enter grade for model 1: "))
model_2= float(input(f"Enter grade for model 2: "))
model_3= float(input(f"Enter grade for model 3: "))
model_4= float(input(f"Enter grade for model 4: "))
model_5= float(input(f"Enter grade for model 5: "))
model_6= float(input(f"Enter grade for model 6: "))
# append the grades 
Grades.append(model_1)
Grades.append(model_2)
Grades.append(model_3)
Grades.append(model_4)
Grades.append(model_5)
Grades.append(model_6)
# using min max and sum statement to print outputs 
highest_grade= max(Grades)
print(highest_grade)
lowest_grade = min(Grades)
print(lowest_grade)
sum_of_grade = sum(Grades)
print(sum_of_grade)
Average = sum(Grades)/len(Grades)
print( Average)
print("-----------------Results------------")
print(f"{'lowest Grade:':<15} {lowest_grade:>20}")
print(f"{'highest Grade:':<15} {highest_grade:>20}")
print(f"{'sum of Grade:':<15} {sum_of_grade:>20}")
print(f"{'Average:':<15} {Average:>20.2f}")
print("---"*20)
#using if else and elifs to get a letter grade 
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
print( f"your grade is: {f_grade}") 
    

