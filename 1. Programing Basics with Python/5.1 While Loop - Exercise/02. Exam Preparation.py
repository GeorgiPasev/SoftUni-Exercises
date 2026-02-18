number_of_weak_grades_to_fail = int(input())
name_of_exercise = input()
weak_grade_counter = 0
grade_counter = 0
sum_grades = 0

while name_of_exercise != "Enough":
    current_exercise_grade = int(input())
    grade_counter += 1
    sum_grades += current_exercise_grade
    if current_exercise_grade <= 4:
        weak_grade_counter += 1
        if weak_grade_counter == number_of_weak_grades_to_fail:
            break
    last_exercise = name_of_exercise
    name_of_exercise = input()


if name_of_exercise == "Enough":
    average_score = sum_grades / grade_counter
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {grade_counter}")
    print(f"Last problem: {last_exercise}")
elif weak_grade_counter == number_of_weak_grades_to_fail:
    print(f"You need a break, {number_of_weak_grades_to_fail} poor grades.")