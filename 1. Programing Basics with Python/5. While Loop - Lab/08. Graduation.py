name_of_student = input()

skusan = 0
year = 1
sum_grades = 0

while year <= 12:
    yearly_grades = float(input())
    if yearly_grades < 4:
        skusan += 1
        if skusan == 2:
            break
        continue
    
    sum_grades += yearly_grades

    year += 1

if skusan == 2:
    print(f"{name_of_student} has been excluded at {year} grade")
else:
    average = sum_grades / 12
    print(f"{name_of_student} graduated. Average grade: {average:.2f}")

