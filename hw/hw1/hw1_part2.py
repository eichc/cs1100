# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 18:10:30 2022

@author: eichc

Calculate a runner's average pace and speed.
"""
#ask for all inputs and convert to int/float
minutes = input("Minutes ==> ").strip()
print(minutes)
minutes = int(minutes)

seconds = input("Seconds ==> ").strip()
print(seconds)
seconds = int(seconds)

milesRun = input("Miles ==> ").strip()
print(milesRun)
milesRun = float(milesRun)

targetMiles = input("Target Miles ==> ").strip()
print(targetMiles)
targetMiles = float(targetMiles)


#calculate the pace
timeInSeconds = minutes*60 + seconds
secondsPerMile = timeInSeconds / milesRun
paceMinutes = int(secondsPerMile // 60)
paceSeconds = int(secondsPerMile % 60)

#calculate the speed
milesPerSecond = milesRun / timeInSeconds
mph = milesPerSecond * 3600

#calculate the time to run to target
timeToTarget = targetMiles * secondsPerMile
targetMinutes = int(timeToTarget // 60)
targetSeconds = int(timeToTarget % 60)


#print the calculations
print("")
print("Pace is", paceMinutes, "minutes and", paceSeconds, "seconds per mile.")
print("Speed is {:.2f} miles per hour.".format(mph))
print("Time to run the target distance of {:.2f} miles is".format(targetMiles), 
      targetMinutes, "minutes and", targetSeconds, "seconds.")