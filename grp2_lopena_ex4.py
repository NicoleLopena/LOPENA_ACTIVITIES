score = int(input("Enter your score: "))

if score > 90:
    grade = 'A'

elif score > 75:
    grade = 'B'

elif score > 65:
    grade = 'C'

else:
    grade = 'D'

print(f"Your grade is: {grade}")