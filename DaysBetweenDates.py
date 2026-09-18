from datetime import date

date1 = date(2014, 7, 2)
date2 = date(2014, 7, 11)

delta = abs(date2 - date1)

print(f"The number of days between two dates is : {delta.days}")