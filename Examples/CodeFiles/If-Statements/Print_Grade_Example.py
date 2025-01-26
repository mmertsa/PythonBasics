def get_grade(score):
    if not 0 <= score <= 100:
        return "The score is not possible."
    elif score < 51:
        return "Grade: 0"
    elif score < 61:
        return "Grade: 1"
    elif score < 71:
        return "Grade: 2"
    elif score < 81:
        return "Grade: 3"
    elif score < 91:
        return "Grade: 4"
    else:
        return "Grade: 5"

score = float(input("Enter your score: "))
print(get_grade(score))