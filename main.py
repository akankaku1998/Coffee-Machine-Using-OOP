from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

turn_off = False
while not turn_off:
  option = menu.get_items()
  choice = input(f'What would you like? ({option}): ').lower()
  if choice == 'off':
    turn_off = True
  elif choice == "report":
    coffee_maker.report()
    money_machine.report()
  else:
    drink = menu.find_drink(choice)
    if coffee_maker.is_resource_sufficient(drink):
      if money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)