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




#todo process coins, create math function


