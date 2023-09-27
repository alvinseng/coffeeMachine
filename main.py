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


def resource_check():
    return f"water: {p.resources['water']} \nmilk: {p.resources['milk']} \ncoffee: {p.resources['coffee']}"

def resource_usage(resource, required_ingredients):
    for ingredient, amount in required_ingredients.items():
        if resource.get(ingredient, 0) < amount:
            print("Not enough ingredients")
            return False
    return True

def make_drink(choice, resource, required_ingredients):
    for ingredient, amount in required_ingredients.items():
        resource[ingredient] -= amount


def coffee_machine():
    money = 0
    machine = True
    menu = p.MENU
    resource = p.resources

    while machine:
        customerOrder = input("Welcome! What would you like to order? (espresso/latte/cappuccino): ").lower()

        if customerOrder == "off":
            clear()
            print("Machine is turning off")
            break
        elif customerOrder == "resource":
            print(resource_check())
            print(f"money:${money}")
        if customerOrder in menu:
            if resource_usage(resource, menu[customerOrder]["ingredients"]):
                cost = menu[customerOrder]["cost"]
                print(f"Cost of {customerOrder}: ${cost}\n")
                money += cost
                if customer_change(coinInput(), cost): # calculates the money input to calculate change
                    print(f"Here is your {customerOrder} ☕, Enjoy!")
            else:
                print("Not enough ingredients")
        else:
            print("Invalid order. Try Again")


coffee_machine()