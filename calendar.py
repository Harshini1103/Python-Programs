import calendar
year=int(input("Enter Year:"))
month=int(input("Enter Month:"))
cal=calendar.month(year,month)
print(cal)
# output:
# Enter Year:2002
# Enter Month:12
#    December 2002
# Mo Tu We Th Fr Sa Su
#                    1
#  2  3  4  5  6  7  8
#  9 10 11 12 13 14 15
# 16 17 18 19 20 21 22
# 23 24 25 26 27 28 29
# 30 31
