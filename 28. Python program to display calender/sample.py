import calendar # Importing calender module 

year = int(input("Enter year: "))
month = int(input("Enter month: "))

calendar = calendar.month(year,month)  #display calender variable that takes year and month 
print(calendar)