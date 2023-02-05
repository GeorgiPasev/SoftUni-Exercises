def solve(grade):
    if 2 <= grade <= 2.99:
        return 'Fail'
    if 3 <= grade <= 3.49:
        return 'Poor'
    if 3.5 <= grade <= 4.49:
        return 'Good'
    if 4.5 <= grade <= 5.49:
        return 'Very Good'
    if 5.5 <= grade <= 6.00:
        return 'Excellent'


grade_data = float(input())
print(solve(grade_data))

#Alternative
def solve(grade):
    result = ''
    if 2 <= grade <= 2.99:
        result = 'Fail'
    if 3 <= grade <= 3.49:
        result = 'Poor'
    if 3.5 <= grade <= 4.49:
        result = 'Good'
    if 4.5 <= grade <= 5.49:
        result = 'Very Good'
    if 5.5 <= grade <= 6.00:
        result = 'Excellent'
    
    return result


grade_data = float(input())
print(solve(grade_data))