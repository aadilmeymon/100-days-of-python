student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
total_height=0
number_of_students=0
for h in student_heights:
    total_height += h
    number_of_students+=1
avg_height=round(total_height/number_of_students)
print(f"Average of heights is: {avg_height}.")