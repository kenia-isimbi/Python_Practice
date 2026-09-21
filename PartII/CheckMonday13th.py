from datetime import date

def test(month, year): 
    
    is_monday_13th = date(year, month, 13).strftime("%A") == 'Monday'
    
    return str(is_monday_13th)

month = 11
year = 2022

print("Month No.: ", month, " Year: ", year)

print("Check whether the said month and year contain a Monday 13th.: " + test(month, year))


month = 6
year = 2022

print("\nMonth No.: ", month, " Year: ", year)

print("Check whether the said month and year contain a Monday 13th.: " + test(month, year))
