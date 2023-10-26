import products as p
import os

profit = 0
os.system('cls')
def clear():
     os.system('cls' if os.name == 'nt' else 'clear')

def coinInput():
    print("Please Insert Coins.")
    q_sum = int(input("How many Quarters?: ")) * 0.25
    d_sum = int(input("How many Dimes?: ")) * 0.10
    n_sum = int(input("How many Nickles?: ")) * 0.05
    p_sum = int(input("How many Pennies?: ")) * 0.01
    # print(f"quarters total: {q_sum}, dime total: {d_sum}, nickle total: {n_sum}, pennies total: {p_sum}")
    total= round(q_sum + d_sum + n_sum + p_sum, 2)
    print(f"Total amount inserted: ${total}")
    return total


def customer_change(total, cost):
    if total >= cost:
        global profit
        profit += cost
        change = total - cost
        print(f"Your change is: ${change}")
        return change
    else:
        print("Incorrect amount. Money Refunded.")


def resource_check(resources):
    return f"water: {p.resources['water']} \nmilk: {p.resources['milk']} \ncoffee: {p.resources['coffee']}"

def resource_usage(resources, required_ingredients):
    for ingredient, amount in required_ingredients.items():
        if resources.get(ingredient, 0) < amount:
            print(f"Not enough {ingredient}")
            return False
    return True

def make_drink(choice, resources, required_ingredients):
    for ingredient, amount in required_ingredients.items():
        resources[ingredient] -= amount


def coffee_machine():
    menu = p.MENU
    resource = p.resources

    while True:
        customerOrder = input("Welcome! What would you like to order? (espresso/latte/cappuccino): ").lower()

        if customerOrder == "off":
            clear()
            print("Machine is turning off")
            break
        elif customerOrder == "report":
            print(resource_check(resource))
            print(f"profit: ${profit}")
        if customerOrder in menu:
            if resource_usage(resource, menu[customerOrder]["ingredients"]):
                cost = menu[customerOrder]["cost"]
                print(f"Cost of {customerOrder}: ${cost}\n")
                if customer_change(coinInput(), cost): # calculates the money input to calculate change
                    make_drink(customerOrder, resource, menu[customerOrder]["ingredients"])
                    print(f"Here is your {customerOrder} ☕, Enjoy!")
            else:
                print("Not enough ingredients")
        else:
            print("Invalid order. Try Again")


coffee_machine()