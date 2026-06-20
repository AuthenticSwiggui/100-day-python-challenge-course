from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_handler = Menu()
coffee_maker_handler = CoffeeMaker()
money_handler = MoneyMachine()
user_choice = ""

def brewing_coffee(choice) -> None:
    if money_handler.make_payment(choice.cost) and coffee_maker_handler.is_resource_sufficient(choice):
        coffee_maker_handler.make_coffee(choice)
    return
    
def coffee_machine():
    while True:
        print("*" * 60)
        print("Welcome to this weird coffee machine!")
        print("What do you want today?")

        print(menu_handler.get_items())
        option = input("").lower()
        if option == "off":
            print("GoodBye!")
            exit()
        if option == "report":
            coffee_maker_handler.report()
            print("*" * 60)
            money_handler.report()
            continue
        user_choice = menu_handler.find_drink(option)
        if user_choice:
            brewing_coffee(choice=user_choice)

if __name__ == "__main__":
    try:
        coffee_machine()
    except KeyboardInterrupt:
        exit()

        
    
