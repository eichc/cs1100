# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 11:09:54 2022

@author: Cam Eich

Using data from covidtracking.com, allow a user to select a certain week's 
Covid-19 data. Provide the user with a number of ways to view the data of either
one specific state or of all 50 states plus DC and Puerto Rico.
"""

import hw4_util

def calc_daily(state_index, week_data):
    '''
    Given a state's index and a week's data, calculate and return the average 
    daily positive cases per 100k people of that state.
    '''
    state_data = week_data[state_index]
    pop = state_data[1]
    total_pos = 0
    for i in range(2, 9): #sum the positive cases across all 7 days
        total_pos += state_data[i]
    daily_avg = total_pos / 7
    avg_100k = daily_avg * 100000 / pop
    avg_100k = round(avg_100k, 1)
    return avg_100k

def calc_pct(state_index, week_data):
    '''
    Given a state's index and a week's data, calculate and return the average
    daily percentage of tests that are positive for that state.
    '''
    state_data = week_data[state_index]
    #sum the positive cases across all 7 days
    total_pos = 0
    for i in range(2, 9):
        total_pos += state_data[i]
    #sum the negative cases across all 7 days
    total_neg = 0
    for i in range(9, len(state_data)):
        total_neg += state_data[i]
        
    percentage = total_pos / (total_pos + total_neg) * 100
    percentage = round(percentage, 1)
    return percentage

def calc_quar(week_data):
    '''
    Given a week's data, return a list of all of the quarantine states for
    that week.
    '''
    quar_states = []
    for i in range(len(week_data)):
        if calc_daily(i, week_data) > 10 or calc_pct(i, week_data) > 10:
            quar_states.append(week_data[i][0])
    return quar_states

def calc_high(week_data):
    '''
    Given a week's data, calculate the state with the highest average daily 
    cases per 100k people. Return a tuple containing the state's abbreviation
    and its average daily cases.
    '''
    high_state = ''
    high_daily = 0
    for i in range(len(week_data)):
        if calc_daily(i, week_data) > high_daily:
            high_daily = calc_daily(i, week_data)
            high_state = week_data[i][0]
    return (high_state, high_daily)


if __name__ == "__main__":
    index = 1
    while index > 0:
        #initial input
        print("...")
        index = input("Please enter the index for a week: ").strip()
        print(index)
        index = int(index)
        
        #skip this if index is less than 1, therefore ending the loop
        if index > 29:
            print("No data for that week")
        elif 1 <= index <= 29:
            req = input("Request (daily, pct, quar, high): ").strip()
            print(req)
            req = req.lower()
        
            week_data = hw4_util.part2_get_week(index)
            
            if req == 'daily':
                state = input("Enter the state: ").strip()
                print(state)
                state = state.upper()
                
                #find the index of the state
                state_index = -1
                for i in range(len(week_data)):
                    if state == week_data[i][0]:
                        state_index = i
                #if the state doesn't exist, print an error message
                if state_index == -1:
                    print("State {} not found".format(state))
                else:
                    daily = calc_daily(state_index, week_data)
                    print("Average daily positives per 100K population:", daily)
            elif req == 'pct':
                state = input("Enter the state: ").strip()
                print(state)
                state = state.upper()
                
                #find the index of the state
                state_index = -1
                for i in range(len(week_data)):
                    if state == week_data[i][0]:
                        state_index = i
                #if the state doesn't exist, print an error message
                if state_index == -1:
                    print("State {} not found".format(state))
                else:
                    pct = calc_pct(state_index, week_data)
                    print("Average daily positive percent:", pct)
            elif req == 'quar':
                quar_states = calc_quar(week_data)
                print("Quarantine states:")
                hw4_util.print_abbreviations(quar_states)
            elif req == 'high':
                high = calc_high(week_data)
                print("State with highest infection rate is", high[0])
                print("Rate is {} per 100,000 people".format(high[1]))
            else:
                print("Unrecognized request")
                
                