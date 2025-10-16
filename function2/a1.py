y1 = int(input("Enter starting year: "))
y2 = int(input("Enter ending year: "))

if y1 > y2:
    print("End year must be greater than or equal to start year")
else:
    print(f"Leap years from {y1} to {y2}")
    for year in range(y1, y2 + 1):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(year)



import datetime
current_year = datetime.date.today().year 
final_year = int(input("Enter the final year: "))
if final_year < current_year:
    print("Final year must be greater than or equal to the current year")
else:
    print (f"Leap years from {current_year} to {final_year}")
    for year in range (current_year, final_year + 1):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(year)
