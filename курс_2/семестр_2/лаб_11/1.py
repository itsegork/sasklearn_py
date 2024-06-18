num_grades = int(input("Введите количество оценок: "))
grades = []
for i in range(num_grades):
    grade = float(input("Введите оценку: "))
    grades.append(grade)
print("Оценки:")
for grade in grades:
    print(grade)
average_grade = sum(grades) / num_grades
print("Средняя оценка:", average_grade)