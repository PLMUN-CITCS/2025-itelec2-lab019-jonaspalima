user_input = input("Enter your numeric grade: ")
grade = int(user_input)
    
if grade > 90:
    letter_grade = "A"
elif grade >= 80:
    etter_grade = "B"
elif grade >= 70:
    letter_grade = "C"
elif grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
    
    print("Your grade is:", letter_grade) # Correct indentation
