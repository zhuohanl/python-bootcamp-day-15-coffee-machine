from data import MENU, resources


def check_resource_sufficient(ingredients):

    # Compare given with required
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry there is no enough {item}.")
            return False

    return True


def process_coins():

    print('Please insert coins.')
    num_quarters = int(input('How many quarters?: '))
    num_dimes = int(input('How many dimes?: '))
    num_nickles = int(input('How many nickles?: '))
    num_pennies = int(input('How many pennies?: '))

    money_inserted = 0.25 * num_quarters + 0.10 * num_dimes + 0.05 * num_nickles + 0.01 * num_pennies

    return money_inserted


def check_transaction_successful(money_inserted, price):
    if money_inserted < price:
        print(f"Sorry that's not enough money. Money refunded.")
        return False

    global money
    money += price

    if money_inserted > price:
        change = round(money_inserted - price, 2)
        print(f'Here is ${change} in change.')

    return True


def make_coffee(ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]

    print(f"Here is your {user_choice} \N{Hot Beverage}. Enjoy!")


money = 0

# 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
# 1a. Check the user’s input to decide what to do next.
# 1b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.
machine_is_on = True
while machine_is_on:

    user_choice = input('What would you like? (espresso/latte/cappuccino): ').lower()

# 2. Turn off the Coffee Machine by entering "off" to the prompt.
# 2a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.
    if user_choice == 'off':
        print('Coffee machine shutting down ...')
        machine_is_on = False

# 3. Print report.
# 3a. When the user enters "report" to the prompt, a report should be generated that
#  shows the current resource values.

    elif user_choice == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")

# 4. Check resources sufficient?
# 4a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
# 4b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine.
#  It should not continue to make the drink but print: "Sorry there is not enough water."
# 4c. The same should happen if another resource is depleted, e.g. milk or coffee.

    elif user_choice in ('espresso', 'latte', 'cappuccino'):

        # Get all ingredients required
        ingredients_required = MENU[user_choice]['ingredients']
        cost = MENU[user_choice]['cost']

        # Check resource sufficient
        is_resource_sufficient = check_resource_sufficient(ingredients_required)

# 5. Process coins.
# 5a. If there are sufficient resources to make the drink selected,
#  then the program should prompt the user to insert coins.
# 5b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# 5c. Calculate the monetary value of the coins inserted.
#  E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
        if is_resource_sufficient:
            payment = process_coins()

# 6. Check transaction successful?
# 6a. Check that the user has inserted enough money to purchase the drink they selected.
# 6b. But if the user has inserted enough money, then the cost of the drink
#  gets added to the machine as the profit and this will be reflected the next time “report” is triggered.
# 6c. If the user has inserted too much money, the machine should offer change.
            is_transaction_successful = check_transaction_successful(payment, cost)

# 7. Make Coffee.
# 7a. If the transaction is successful and there are enough resources to make the drink the user selected,
#  then the ingredients to make the drink should be deducted from the coffee machine resources.
# 7b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”.
#  If latte was their choice of drink.
            if is_transaction_successful:
                make_coffee(ingredients_required)

    else:
        print(f"Your instruction is invalid. Please input one of these: [report, espresso, latte, cappuccino].")
