# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 12:11:07 2022

@author: eichc
"""

from Date import Date

def read_birthdays(file):
    dates = []
    for line in open(file):
        L = line.split()
        year = int(L[0])
        month = int(L[1])
        day = int(L[2])
        date = Date(year, month, day)
        dates.append(date)
    return dates

if __name__ == "__main__":
    birthdays = read_birthdays('birthdays.txt')
    
    #find earliest birthday
    earliest = birthdays[0]
    for i in range(len(birthdays)):
        if birthdays[i] < earliest:
            earliest = birthdays[i]
    print("The earliest birthday is", earliest)
    
    #find the latest birthday
    latest = birthdays[0]
    for i in range(len(birthdays)):
        if not birthdays[i] < latest:
            latest = birthdays[i]
    print("The latest birthday is", latest)
    
    #find month with most birthdays
    month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July',\
                        'August','September', 'October', 'November', 'December' ]
    month_counts = []
    for i in range(len(month_names)):
        month_counts.append(0)
    for date in birthdays:
        month_counts[date.month] += 1
        
    high_name = month_names[0]
    high_count = month_counts[0]
    for i in range(len(month_counts)):
        if month_counts[i] > high_count:
            high_count = month_counts[i]
            high_name = month_names[i]
    print("The month with the most birthdays is", high_name)