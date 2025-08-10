import calendar                     # import calender

def get_calender(yy, mm):           # defining a function with YEAR and Month input Parameter
    return calendar.month(yy, mm)   # Return a particular month in a particular year.

# Calling functuion with actual arguments.
 
bindu_born = print(get_calender(1996,3))
manu_born = print(get_calender(1993,1))

'''
output :
     March 1996
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31

    January 1993
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31

'''
