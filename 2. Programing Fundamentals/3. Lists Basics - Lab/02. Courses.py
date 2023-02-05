number_of_lines = int(input())
list_of_courses = []

for line in range(number_of_lines):
    current_course_name = input()
    list_of_courses.append(current_course_name)

print(list_of_courses)