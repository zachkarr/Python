#! /usr/bin/env python3
# coinbank by Zach Karr

import locale
from UserInput import UserInput
from Bank import Bank

coin_types = ["pennies", "nickles", "dimes", "quarters"]


def get_coin_count():
    global coin_types
    total = []
    for i, coins in enumerate(coin_types):
        amount = []
        coin = UserInput.getInt("How many " + coins + " do you have? ", 0)
        amount = [i, coin]
        total.append(amount)

    return total


def get_coin_total():
    total = get_coin_count()
    pennies = total[0][1]
    nickles = total[1][1]
    dimes = total[2][1]
    quarters = total[3][1]
    bank = Bank(pennies, nickles, dimes, quarters)
    print("The bank is open!")
    get_bank_amount(bank)
    return bank


def action_type(bank):
    choice = -1
    while choice < 0:
        choice = UserInput.getInt(
            "Action: 1=Quarters, 2=Dimes, 3=Nickles, 4=Pennies, 0=Quit: "
        )
        if choice == 0:
            print("Thank you for using the Coin Bank!")
            return -1
        elif choice == 1:
            add_remove_quarters(bank)
        elif choice == 2:
            add_remove_dimes(bank)
        elif choice == 3:
            add_remove_nickles(bank)
        elif choice == 4:
            add_remove_pennies(bank)
        else:
            print("Unknown action type!")
            choice = -1


def get_bank_amount(bank):
    print(
        "Currently in the bank: Quarters = "
        + str(bank.get_quarters())
        + ", "
        + "Dimes = "
        + str(bank.get_dimes())
        + ", "
        + "Nickles = "
        + str(bank.get_nickles())
        + ", "
        + "Pennies = "
        + str(bank.get_pennies())
        + " for a Total of: %s" % locale.currency(bank.get_total(), grouping=True)
    )


def negative_balance(input, coin_type, bank):
    amount_given = ""
    if coin_type == " quarters":
        amount_given = bank.get_quarters()
    elif coin_type == " dimes":
        amount_given = bank.get_dimes()
    elif coin_type == " nickles":
        amount_given = bank.get_nickles()
    elif coin_type == " pennies":
        amount_given = bank.get_pennies()
    else:
        amount_given = 0
    print(
        "I cannot give you "
        + str(input * -1)
        + coin_type
        + "; I have given you "
        + str(amount_given)
        + " instead"
    )


def add_remove_quarters(bank):
    quarters = UserInput.getInt(
        "Add or Remove quarters (pos # to add, neg # to remove: ) "
    )
    if bank.get_quarters() + quarters < 0:
        negative_balance(quarters, " quarters", bank)
        bank.set_quarters(bank.get_quarters() + (quarters + 1))
        if bank.get_quarters() < 0:
            bank.set_quarters(0)
        get_bank_amount(bank)
    if bank.get_quarters() >= 0 and quarters > 0:
        bank.set_quarters(bank.get_quarters() + quarters)
        print(str(quarters) + " added to the bank.")
        get_bank_amount(bank)
    elif bank.get_quarters() > 0 and quarters < 0:
        bank.set_quarters(bank.get_quarters() + quarters)
        print(str(quarters) + " removed from the bank")
        get_bank_amount(bank)
    action_type(bank)


def add_remove_dimes(bank):
    dimes = UserInput.getInt("Add or Remove Dimes (pos # to add, neg # to remove: ) ")
    if bank.get_dimes() + dimes < 0:
        negative_balance(dimes, " dimes", bank)
        bank.set_dimes(bank.get_dimes() + (dimes + 1))
        if bank.get_dimes() < 0:
            bank.set_dimes(0)
        get_bank_amount(bank)
    if bank.get_dimes() >= 0 and dimes > 0:
        bank.set_dimes(bank.get_dimes() + dimes)
        print(str(dimes) + " added to the bank.")
        get_bank_amount(bank)
    elif bank.get_dimes() > 0 and dimes < 0:
        bank.set_dimes(bank.get_dimes() + dimes)
        print(str(dimes) + " removed from the bank")
        get_bank_amount(bank)

    action_type(bank)


def add_remove_nickles(bank):
    nickles = UserInput.getInt(
        "Add or Remove Nickles (pos # to add, neg # to remove: ) "
    )
    if bank.get_nickles() + nickles < 0:
        negative_balance(nickles, " nickles", bank)
        bank.set_nickles(bank.get_nickles() + (nickles + 1))
        if bank.get_nickles() < 0:
            bank.set_nickles(0)
        get_bank_amount(bank)
    if bank.get_nickles() >= 0 and nickles > 0:
        bank.set_nickles(bank.get_nickles() + nickles)
        print(str(nickles) + " added to the bank.")
        get_bank_amount(bank)
    elif bank.get_nickles() > 0 and nickles < 0:
        bank.set_nickles(bank.get_nickles() + nickles)
        print(str(nickles) + " removed from the bank")
        get_bank_amount(bank)

    action_type(bank)


def add_remove_pennies(bank):
    pennies = UserInput.getInt(
        "Add or Remove Pennies (pos # to add, neg # to remove: ) "
    )
    if bank.get_pennies() + pennies < 0:
        negative_balance(pennies, " pennies", bank)
        bank.set_pennies(bank.get_pennies() + (pennies + 1))
        if bank.get_pennies() < 0:
            bank.set_pennies(0)
        get_bank_amount(bank)
    if bank.get_pennies() >= 0 and pennies > 0:
        bank.set_pennies(bank.get_pennies() + pennies)
        print(str(pennies) + " added to the bank.")
        get_bank_amount(bank)
    elif bank.get_pennies() > 0 and pennies < 0:
        bank.set_pennies(bank.get_pennies() + pennies)
        print(str(pennies) + " removed from the bank")
        get_bank_amount(bank)

    action_type(bank)


def main():
    result = locale.setlocale(locale.LC_ALL, "")
    if result == "C" or result.startswith("C/"):
        locale.setlocale(locale.LC_ALL, "en_US")
    print("Welcome to the Coin Bank")
    print("Enter the coin counts to start the bank:")
    bank = get_coin_total()
    action = action_type(bank)
    if action == -1:
        return


if __name__ == "__main__":
    main()
