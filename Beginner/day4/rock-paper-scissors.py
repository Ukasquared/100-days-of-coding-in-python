#!/usr/bin/python3
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# get the user input
user_input = int(input(f"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.    "))

# generate a random number between 0 to 2
random_number = random.randint(0, 2)
# let ses if a method will work
def who_wins():
    if random_number == 0:
        print(f"{rock}\nIts a draw")
    elif random_number == 1:
        print(f"{paper}\nYou lose")
    elif random_number == 2:
        print(f"{scissors}\n You win")
# compare the random_number generated with the user input
# rock wins against scissors, scissors wins against papar, paper win against rock
if user_input == 0:
    print(f"{rock} \n computer chose")
    who_wins()

if user_input == 1:
    print(f"{paper} \n computer chose")
    who_wins()

if user_input == 2:
    print(f"{scissors} \n computer chose")
    who_wins()
