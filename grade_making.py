marks =int(input('Enter the value of marks: '))

if marks >= 80:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 70:
    grade = "A-"
elif marks >= 65:
    grade = 'B+'
elif marks >= 60:
    grade = "B"
elif marks >= 55:
    grade = "B-"
elif marks >= 50:
    grade = "C+"
elif marks >= 45:
    grade = 'C'
elif marks >= 40:
    grade = "D"
else:
    grade= 'Fail'

print("Your grade is ",grade)