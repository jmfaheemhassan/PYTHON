years=2029
if (years%4==0) and (years%100!=0):
    print("{0} is a leap year".format(years))
elif (years%400==0) and (years%100==0):
    print("{0} is a leap year".format(years))
else:
    print("{0} is not a leap year".format(years))