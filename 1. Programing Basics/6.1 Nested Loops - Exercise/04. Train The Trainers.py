jury_number = int(input())
presentation_name = input()
sum_all_grades = 0
presentation_number = 0

while presentation_name != "Finish":
    grade_counter = 0
    sum_grades = 0
    for grade in range(jury_number):
        current_grade = float(input())
        sum_grades += int(current_grade * 100)
        grade_counter += 1
    current_presentation_average = sum_grades / grade_counter
    sum_all_grades += current_presentation_average
    print(f"{presentation_name} - {current_presentation_average / 100:.2f}.")
    presentation_number += 1
    presentation_name = input()

final_assessment_average = sum_all_grades / presentation_number
print(f"Student's final assessment is {(final_assessment_average / 100):.2f}.")
    

