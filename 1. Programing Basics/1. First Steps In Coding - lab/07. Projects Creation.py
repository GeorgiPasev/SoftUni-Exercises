# input name of architect
# input number of projects whole number
# print ⦁	"The architect {името на архитекта} will need 
# {необходими часове} hours to complete {брой на проектите} project/s."

name = input()
number_of_projects = int(input())
hours = 3 * number_of_projects
print(f"The architect {name} will need {hours} hours to complete {number_of_projects} project/s.")
