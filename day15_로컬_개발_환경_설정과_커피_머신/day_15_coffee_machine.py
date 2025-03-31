# TODO: 1. Print report of all coffee machine resources\
from coffee_logo import logo
coffee_run = True

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO Check resources sufficient?
def resources_check(want_manu):
    """ 재료 재고 확인 함수"""
    if want_manu == "espresso":
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
    elif want_manu == "latte":
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
    elif want_manu == "cappuccino":
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]

    if resources["water"] <= 0:
        return "water"
    elif resources["coffee"] <= 0:
        return "coffee"
    elif resources["milk"] <= 0:
        return "milk"
    else:
        return 0


# TODO Process coins
def coin_transaction(quarter, dime, nickel, pennie):
    """ 동전들 달러 단위로 변환"""
    quarter = (quarter * 25) * 0.01
    dime = (dime * 10) * 0.01
    nickel = (nickel * 5) * 0.01
    pennie = (pennie * 1) * 0.01
    coin_in_dollar = quarter + nickel + pennie + dime
    return coin_in_dollar


# TODO 금액 계산
def cal_cost(want_manu, user_pay):
    """금액 계산하는 함수"""
    change = 0

    if want_manu == "espresso":
        change = user_pay - MENU["espresso"]["cost"]
    elif want_manu == "latte":
        change = user_pay - MENU["latte"]["cost"]
    elif want_manu == "cappuccino":
        change = user_pay - MENU["cappuccino"]["cost"]

    return change


# TODO Make Coffee
def system():
    # 메뉴 고르기
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if not (user_input == "espresso" or user_input == "latte" or user_input == "cappuccino"):
        print("try again")
        return 1

    # 재료 확인하기
    enough = resources_check(user_input)
    if not (enough == 0):
        print(f"Sorry there is not enough {enough}")
        return 1
    print("Please insert coins.")

    # 코인 받고 달러로 변환
    quarters = int(input("  How many quarters?: "))
    dimes = int(input("  How many dimes?: "))
    nickels = int(input("  How many nickels?: "))
    pennies = int(input("  How many pennies?: "))
    user_pay = coin_transaction(quarters, dimes, nickels, pennies)
    round(user_pay, 2)
    print(user_pay)

    # 금액 계산
    change = cal_cost(user_input, user_pay)
    if change < 0:
        print("Sorry that's not enough money. Money refunded")
        return 1
    else:
        print(f"Here is ${change} in change.")

    # 메뉴 건네기
    print(f"Here is your {user_input}. Enjoy!")


def main():
    print(logo)

    while coffee_run:
        system()

main()
