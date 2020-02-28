import Grades

s_name = input("Please enter Student name: ")

homework = float(input("Please enter Homework mark: "))
assessment = float(input("Please enter Assessment mark: "))
final_exam = float(input("Please enter Final Exam mark: "))

print(s_name, Grades.ict_fun(homework,assessment,final_exam))