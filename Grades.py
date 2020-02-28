s_name = input("Please enter Student name: ")

homework = float(input("Please enter Homework mark: "))
assessment = float(input("Please enter Assessment mark: "))
final_exam = float(input("Please enter Final Exam mark: "))

def ict_fun(homework,assessment,final_exam):
    if homework > 25.0:
        return "Homework mark can't be more than 25"
    elif assessment > 50.0:
        return "Assessment mark can't be more than 50"
    elif final_exam > 100.0:
        return "Assessment mark can't be more than 100"
    else:
        ict = (((homework/25) + (assessment/50) +(final_exam/100))/3)*100
    return ict

print(s_name, ict_fun(homework,assessment,final_exam))