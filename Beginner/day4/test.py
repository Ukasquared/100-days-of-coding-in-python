#!/usr/bin/python3
import random

# user input
random_seed = int(input(f"type a random number  "))
customer_names = input(f"type the names of every who ate a meal?  ")
name_list = customer_names.split(", ")

# generates the same random number every time the code is ran
random.seed(random_seed)
total_num_of_customer = len(name_list)
# generates a random number
random_number = random.randint(0, total_num_of_customer - 1)

# who will pay for the meal
print(f"{name_list[random_number]} will pay for the meal!!!")