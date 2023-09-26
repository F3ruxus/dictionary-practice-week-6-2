# Alright, let's simplify and rephrase the problem set to avoid using functions:
import student_data

# print(student_data.students)
students = student_data.students
print(len(students))
print(students[0]["Combo,Name"])
print(students[0]["CPSID"])
print(students[0]["Email"][0])
print(students[0]["Email"][1])
print(students[1]["Combo,Name"])
print(students[1]["CPSID"])
print(students[1]["Email"][1])
print(students[2]["Combo,Name"])
print(students[2]["CPSID"])
print(students[2]["Email"][1])


#for loops allow us to 
# iterate through the data
# and perform some function

# the student in the for loop is the iterator

for student in students:
  print(student["Combo,Name"])
  print(student["CPSID"])
  print(student["Email"][0])
  print(student["Email"][1])
  print("_"*25)