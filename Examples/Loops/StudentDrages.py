# A short program to calculate grades of students. Do not enter too large
# number for students as you have to enter every students grade one by one :D

number_of_students = int(input("Enter the number of students:\n"))
total_sum = 0
average = 0

for i in range(number_of_students):
    grade = int(input("Enter the student's grade:\n"))
    total_sum = total_sum + grade
    average = round(total_sum / number_of_students, 1)

print(f"Average: {average}")

if 0 <= average < 1:
    print("Poor result")
elif 1 <= average < 2:
    print("Weak result")
elif 2 <= average < 3:
    print("Satisfactory result")
elif 3 <= average < 4:
    print("Good result")
elif 4 <= average <= 5:
    print("Excellent result")
