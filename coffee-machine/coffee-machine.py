from data import MENU, resources
PROFIT = 0


def resource_sufficient(drink_ordered):
    for item in drink_ordered:
        if drink_ordered[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coin():
    print("Please insert coins.")
    total = int(input("How many Quarters?: ")) * 0.25
    total += int(input("How many Dimes?: ")) * 0.1
    total += int(input("How many Nickles?: ")) * 0.05
    total += int(input("How many Pennies?: ")) * 0.01
    return total


def is_transaction_successful(received_amount, order_amount):
    if received_amount > order_amount:
        change = round(received_amount - order_amount, 2)
        print(f"Here is ${change} in change.")
        global PROFIT
        PROFIT += order_amount
        return True
    else:
        print(f"Sorry that's not enough. Take your money back.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


ON = True
while ON:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        ON = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}mg")
        print(f"Money: S{PROFIT}")
    else:
        drink = MENU[choice]
        if resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
print("Thanks for letting us serve you!")
