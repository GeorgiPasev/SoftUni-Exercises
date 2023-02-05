centuries = int(input())

years = 100 * centuries
days = int(365.2422 * years)
hours = 24 * days
minutes = 60 * hours

print(f"{centuries} centuries = {years:.0f} years = {days:.0f} days = {hours:.0f} hours = {minutes:.0f} minutes")