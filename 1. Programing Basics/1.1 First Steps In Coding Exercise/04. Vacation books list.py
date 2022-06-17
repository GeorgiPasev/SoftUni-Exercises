# input number of pages in current book int
# input pages read for 1 hour int
# input number of days needed to read the book int
# print number of hours per day for literature 

pages_in_book = int(input())
pages_read = int(input())
days_needed = int(input())
number_of_hours_per_day = pages_in_book / pages_read / days_needed
print(int(number_of_hours_per_day))
