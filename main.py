import function
import products as p
import function as f


#functions

def coffeeOrder():
    order = ""
    order += customerOrder
    return f"{customerOrder}"

def resourceOutput():
    water = p.resources["water"]
    milk = p.resources["milk"]
    coffee = p.resources["coffee"]
    money = 0
    return f"water: {water} \nmilk: {milk} \ncoffee: {coffee} \nmoney: ${money}"


#todo resource tracker/ report



#Todo 1 create a prompt for user
customerOrder = input(" What would you like? (espresso/latte/cappuccino): ".lower())
if customerOrder == "resource":
    print(resourceOutput())

print(coffeeOrder())


f.coinInput()


#todo 2 Turns off coffee machine using "Off"






#todo 5 check transaction

