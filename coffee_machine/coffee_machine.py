from coffee_menu import MENU

QUARTERS_VALUE = 25
DIMES_VALUE = 10
NICKLES_VALUE = 5
PENNIES_VALUE = 1

coffee_machine = {
    "ingredients_on_machine": {
        "water": 300,
        "milk": 200,
        "coffee": 100
    },
    "machine_income": 0.0
}

#TODO 1 User selects a coffee
def salute() -> str:
    print("SALUTEEEE!!!")
    while True:
        print("Seleccioná un cafesito, y ojito si la quieres con lechita jeejej")
        for coffee_name, values in MENU.items():
            print("*" * 60)
            print(coffee_name.capitalize())
            print("Ingredients:")
            for ingredient, quantity in values["ingredients"].items():
                print(f"{ingredient}: {quantity}")
            print(f"Cost: ${values['cost'] / 100:.2f}")
        user_selection = input("¿Cual deseas?\n").lower()
        if user_selection == "off":
            print("Chao Chao")
            exit()
        if user_selection == "report":
            print_report()
            continue
        if user_selection in MENU:
            return user_selection
        print("Sea serio mano, escoja un cafesito de la máquina")

#TODO 2 Check if coffee machine has enough resources for the coffee
def enough_ingredients(selected_coffee: dict[str, int], current_ingredients: dict[str, int]) -> bool:
    insufficient_ingredients = []
    for ingredient, amount_needed in selected_coffee.items():
        if amount_needed > current_ingredients.get(ingredient, 0):
            insufficient_ingredients.append(f"Sorry, there is not enough {ingredient}")

    for error in insufficient_ingredients:
        if error:
            print(error)
    return not insufficient_ingredients

#TODO 3 User inserts coins
def insert_coins(coins: dict[str, int], cost_cents: int) -> int:
    total_cents = 0
    while True:
        total_cents = coin_multiplier(coins, total_cents)
        if total_cents > cost_cents:
            print(f"Has insertado ${total_cents / 100:.2f}")
            change_cents = total_cents - cost_cents
            return_change(change_cents)
            return cost_cents
        if total_cents == cost_cents:
            return total_cents
        print(f"Porfa insertá más moneditas, faltan ${(cost_cents - total_cents) / 100:.2f}")

def return_change(change_cents: int) -> None:
    change_coins = {
        "quarters": 0,
        "dimes": 0,
        "nickles": 0,
        "pennies": 0
    }
    print(f"Your change is ${change_cents / 100:.2f}")
    while change_cents > 0:
        if change_cents >= QUARTERS_VALUE:
            change_coins["quarters"] += 1
            change_cents -= QUARTERS_VALUE
        elif change_cents >= DIMES_VALUE:
            change_coins["dimes"] += 1
            change_cents -= DIMES_VALUE
        elif change_cents >= NICKLES_VALUE:
            change_coins["nickles"] += 1
            change_cents -= NICKLES_VALUE
        elif change_cents >= PENNIES_VALUE:
            change_coins["pennies"] += 1
            change_cents -= PENNIES_VALUE
            
    for coin_type, coins in change_coins.items():
        print(f"{coin_type}: {coins}")

def coin_multiplier(coins: dict[str, int], total_cents: int) -> int:
    print("Insert coins:")
    for key in coins:
        coins[key] = coin_checker(key)
        if key == "quarters":
            total_cents += coins[key] * QUARTERS_VALUE
        if key == "dimes":
            total_cents += coins[key] * DIMES_VALUE
        if key == "nickles":
            total_cents += coins[key] * NICKLES_VALUE
        if key == "pennies":
            total_cents += coins[key] * PENNIES_VALUE
    return total_cents

def coin_checker(coin_type: str) -> int:
    while True:
        try:
            num_coins = int(input(f"How many {coin_type}?: "))
            if num_coins >= 0:
                return num_coins
            print("Sea serio mano, inserte números positivos")
        except ValueError:
            print("Insertá un número weon")

#TODO 4 Machine pours the coffee operating initial resources - coffee poured refreshing the machine resources
def pour_coffee(choice_ingredients: dict, machine_ingredients: dict[str, int], choice_name: str) -> dict[str, int]:
    print(f"Pouring your coffee!!!")
    print(f"Preparing your {choice_name}")
    for ingredient, amount in choice_ingredients.items():
        machine_ingredients[ingredient] -= amount
    return machine_ingredients

#TODO 5 Print report
def print_report() -> None:
    ingredients = "ingredients_on_machine"
    incomes = "machine_income"
    print("=" * 60)
    print("Coffee Machine Report")
    for element in coffee_machine:
        if element == ingredients:
            print("*" * 60)
            print("Ingredients")
            for ingredient, ingredient_quantity in coffee_machine[ingredients].items():
                print(f"-{ingredient.capitalize()}: {ingredient_quantity}")
            continue
        if element == incomes:
            print(f"{element}: ${coffee_machine[incomes]:.2f}")
        
    input("Press any key to exit from report")

def main():
    inserted_coins = {
        "quarters": 0,
        "dimes": 0,
        "nickles": 0,
        "pennies": 0
    }
    while True:
        print("Welcome to the Coffee Machine!")
        choice_key = salute()
        choice = MENU[choice_key]
        if not enough_ingredients(choice["ingredients"], coffee_machine["ingredients_on_machine"]):
            print("There are no enough ingredients for this coffee")
            continue
        income_cents = insert_coins(inserted_coins, choice["cost"])
        coffee_machine["machine_income"] = round(
            coffee_machine["machine_income"] + income_cents / 100, 2
        )
        coffee_machine["ingredients_on_machine"] = pour_coffee(choice["ingredients"], coffee_machine["ingredients_on_machine"], choice_key)
        more_coffee = input("Another coffee? y/n\n").lower()
        if more_coffee in ["n", "no"]:
            break
    print(f"Total income: ${coffee_machine['machine_income']:.2f}")
    print("See you later!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()