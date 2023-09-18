

""""Machine should be able to turn off after the words 'off' for maintenance"""
def store_check():
    if customerOrder == "resource":
        print(resourceOutput(p))
    elif customerOrder == "off":
        print("Machine is turning off")
        return False


"""Dispense custome change after the order has been completed """


#todo 0: insufficient change, prompts refund

#todo 1: have report print updated information

#todo 2: when order is complete, subtract resources from stock

#todo 3:Add a 'restock' option to refill

#todo 4: checking resources before completing a transaction

