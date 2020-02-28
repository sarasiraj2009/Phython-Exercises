score = float(input("Please enter score: ")) 
def grade(s_grade):
    if score >= 70:
        s_grade = "Your score is: 1st"
    elif score >= 60:
        s_grade = "Your score is: 2.1"
    elif score >= 50:
        s_grade = "Your score is: 2.2"
    elif score >= 40:
        s_grade = "Your score is: pass"
    else:
        s_grade = "Your score is: fail"   
    return (s_grade)
print(grade(score))