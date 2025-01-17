'''
Start to the Date class for Lab 9.  This code will not run in Python
until three methods are added:
    __init__,
    __str__
    same_day_in_year
'''

days_in_month = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July',\
                    'August','September', 'October', 'November', 'December' ]

class Date(object):
    def __init__(self, year=1900, month=1, day=1):
        self.year = year
        self.month = month
        self.day = day
        
    def __str__(self):
        return '{}/{:02d}/{:02d}'.format(self.year, self.month, self.day)
    
    def same_day_in_year(self, other):
        return self.month == other.month and self.day == other.day
    
    def is_leap_year(self):
        if (self.year % 100) == 0:
            return (self.year % 400) == 0
        return (self.year % 4) == 0
    
    def __lt__(self, other):
        if self.year == other.year and self.month == other.month:
            return self.day < other.day
        if self.year == other.year:
            return self.month < other.month
        return self.year < other.year


if __name__ == "__main__":
    d1 = Date(1972, 3, 27)
    d2 = Date(1998, 4, 13)
    d3 = Date(1996, 4, 13)
    print("d1: " + str(d1))
    print("d2: " + str(d2))
    print("d3: " + str(d3))
    print("d1.same_day_in_year(d2)", d1.same_day_in_year(d2))
    print("d2.same_day_in_year(d3)", d2.same_day_in_year(d3)) 
    print()
    print("d1.is_leap_year", d1.is_leap_year())
    print("d2.is_leap_year", d2.is_leap_year())
    print()
    print("d1 < d2", d1 < d2)
    print("d2 < d3", d2 < d3)
    print("d1 < d1", d1 < d1)