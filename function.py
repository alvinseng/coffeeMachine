import os
from products import *
import math




os.system('cls')

def clear():
     os.system('cls' if os.name == 'nt' else 'clear')

#todo 1 resource format


def coinInput():
     print("Please Insert Coins. ")
     insertQ = int(input("How many Quarters?:"))
     insertD = int(input("How many Dimes?:"))
     insertN = int(input("How many Nickles?:"))
     insertP = int(input("How many Pennies?:"))
     sum = (insertQ + insertD + insertN + insertP)
     print(sum)
     return sum


def resourceOutput():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = 0
    return f"water: {water} \nmilk: {milk} \ncoffee: {coffee} \nmoney: ${money}"

#todo process coins, create math function


