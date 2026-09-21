# Student Grade Calculator

name = input("Enter your name: ")

maths = float(input("Enter Maths marks: "))
python = float(input("Enter Python marks: "))
data_science = float(input("Enter Data Science marks: "))

total = maths + python + data_science
percentage = total / 3

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage, "%")

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)