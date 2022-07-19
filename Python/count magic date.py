def magic_date(date):
    """
    This function takes in a date as a string in the format mm dd, yyyy and returns True if the date is a magic date and false otherwise
    A magic date is a date where the day multiplied by the month is equal to thhe last two digits of the year
    """
    date=date.split(" ") #the date string is separated into a list in the format["mm", "dd,", "yyyy"]
    date[1]=date[1][:-1] #the "dd," is replaced by "dd"
    months={"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}
    #A dictionary containing all the months in a year as keys with their position as values 
    if months[date[0]]*int(date[1])==int(date[2][-2:]):
        return True
    else:
        return False
def count_magic(year):
    if type(year)!=int or year<10:
        return "Invalid argument"
    if year%4==0 and year%100!=0 or year%4==0 and year%400==0:
        days={"January":range(1,32), "February":range(1,30), "March":range(1,32), "April":range(1,31), "May":range(1,32), "June":range(1,31), "July":range(1,32), "August":range(1,32), "September":range(1,31), "October":range(1,32), "November":range(1,31), "December":range(1,32)}
    else:
        days={"January":range(1,32), "February":range(1,29), "March":range(1,32), "April":range(1,31), "May":range(1,32), "June":range(1,31), "July":range(1,32), "August":range(1,32), "September":range(1,31), "October":range(1,32), "November":range(1,31), "December":range(1,32)}
    #days represents a dictionary containing months as keys and their days as value for both leap years and normal years 
    magic_dates=[]
    for i in days:                                          #loops through each key(month)
        for k in days[i]:                                   #loops through each day in each month
            if magic_date(i +" "+str(k)+","+" "+str(year)): #this reads "if the magic function returns true for the specified date"
                magic_dates.append(i +" "+str(k)+","+" "+str(year))
            else:
                continue
    return magic_dates    
print(count_magic(2020))
