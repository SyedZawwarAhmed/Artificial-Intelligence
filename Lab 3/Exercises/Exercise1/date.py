getDate = lambda dateString : int(dateString.split(":")[0])
getMonth = lambda dateString : int(dateString.split(":")[1]) 
getYear = lambda dateString : int(dateString.split(":")[2]) 

date = "27:02:2023"
print("Date:-", getDate(date))
print("Month:-", getMonth(date))
print("Year:-", getYear(date))