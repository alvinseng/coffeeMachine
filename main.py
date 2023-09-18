import products as p
import os


os.system('cls')
def clear():
     os.system('cls' if os.name == 'nt' else 'clear')


def coinInput():
    print("Please Insert Coins.")
    insert_q = int(input("How many Quarters?: "))
    q_sum = float(insert_q * .25)
    insert_d = int(input("How many Dimes?: "))
    d_sum = float(insert_d * .10)
    insert_n = int(input("How many Nickles?: "))
    n_sum = float(insert_n * .05)
    insert_p = int(input("How many Pennies?: "))
    p_sum = float(insert_p * .01)
    # print(f"quarters total: {q_sum}, dime total: {d_sum}, nickle total: {n_sum}, pennies total: {p_sum}")
    sum = round(q_sum + d_sum + n_sum + p_sum, 2)
    input_sum = sum
    print(f"Total amount inserted: ${input_sum}")
    return input_sum


def customer_change(input_sum, cost):
    if input_sum >= cost:
        change = input_sum - cost
        print(f"Your change is: ${change}")
        return change


def resource_check(p):
    water = p.resources["water"]
    milk = p.resources["milk"]
    coffee = p.resources["coffee"]
    return f"water: {water} \nmilk: {milk} \ncoffee: {coffee}"

# def resource_usage():



def coffee_machine():
    money = 0
    machine = True
    while machine:
        customerOrder = input("Welcome! What would you like to order? (espresso/latte/cappuccino): ").lower()
        if customerOrder in ["espresso", "latte", "cappuccino"]:
            cost = p.MENU[customerOrder]["cost"]
            print(f"Cost of {customerOrder}: ${cost}\n")
            money += cost
            customer_change(coinInput(), cost)  # calculates the money input to calculate change
            print(f"Here is your {customerOrder} ☕, Enjoy!")
        elif customerOrder == "resource":
            print(resource_check(p))
            print(f"money:${money}")
        elif customerOrder == "off":
            print("Machine is turning off")
            return False
        else:
            print("Invalid order.")
            customerOrder



coffee_machine()