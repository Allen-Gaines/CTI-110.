#Allen Gaines
#10/9/24
#P2HW2
# input grades and get the output
Grades = []
model_1= float(input(f"Enter grade for model 1: "))
model_2= float(input(f"Enter grade for model 2: "))
model_3= float(input(f"Enter grade for model 3: "))
model_4= float(input(f"Enter grade for model 4: "))
model_5= float(input(f"Enter grade for model 5: "))
model_6= float(input(f"Enter grade for model 6: "))
Grades.append(model_1)
Grades.append(model_2)
Grades.append(model_3)
Grades.append(model_4)
Grades.append(model_5)
Grades.append(model_6)

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
print("---" *20)
