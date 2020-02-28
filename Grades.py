
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
