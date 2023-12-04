#!/usr/bin/env python3
""" building a tip calculator"""

print("welcome to the tip calculator.")
total_bill = input("what was the total bill? $")
percent = input("what percentage tip would you like to give ? 10, 12, 0r 15? ")
people = input('how many people to split the bill? ')
tip = float(total_bill) * (1 + float(percent) / 100)
pay = tip / int(people)
print('each person should pay ', end="")
print(round(pay, 2))