#! /usr/bin/env python3
# ForeignCurrency By Zach Karr

import locale

rEUR = rGBP = rJPY = rCAD = rRUB = 0.0


def get_rates():
    global rEUR, rGBP, rJPY, rCAD, rRUB
    rEUR = get_one_rate("EUR")
    rGBP = get_one_rate("GBP")
    rJPY = get_one_rate("JPY")
    rCAD = get_one_rate("CAD")
    rRUB = get_one_rate("RUB")


def get_one_rate(prompt):
    rate = -1
    while rate <= 0:
        try:
            rate = float(input(prompt + ": "))
            if rate <= 0:
                print("Rates must be positive")
        except ValueError:
            print("Must enter a numeric value for the exchange rate.")
            rate = -1
    return rate


def get_choice():
    choice = -1
    while choice < 0 or choice > 5 and choice != 9:
        try:
            choice = int(
                input(
                    "Currency? 1=EUR, 2=GBP, 3=JPY, 4=CAD, 5=RUB, 9=New Rates, 0=Quit: "
                )
            )
            if choice < 0 or choice > 5 and choice != 9:
                print("Unknown option: 0-5 or 9 only")
        except ValueError:
            print("Illegal Input must be an input from 0-5 or 9")
    return choice


def do_valuation():
    global rEUR, rGBP, rJPY, rCAD, rRUB
    grand_total = 0.0
    total_currency_units = [0, 0, 0, 0, 0]
    total_currency_value = [0.0, 0.0, 0.0, 0.0, 0.0]
    currency_abbreviations = ["EUR", "GBP", "JPY", "CAD", "RUB"]
    choice = get_choice()
    while choice != 0:
        val = 0.0
        print("Your choice was: " + str(choice))
        if choice == 1:
            qty = get_units("Euros")
            val = rEUR * qty
            print(str(qty) + " Euros = %s " % locale.currency(val, grouping=True))
            total_currency_units[choice - 1] += qty
            total_currency_value[choice - 1] += val
        elif choice == 2:
            qty = get_units("Pounds")
            val = rGBP * qty
            print(str(qty) + " Pounds = %s " % locale.currency(val, grouping=True))
            total_currency_units[choice - 1] += qty
            total_currency_value[choice - 1] += val

        elif choice == 3:
            qty = get_units("Yen")
            val = rJPY * qty
            print(str(qty) + " Yen = %s " % locale.currency(val, grouping=True))
            total_currency_units[choice - 1] += qty
            total_currency_value[choice - 1] += val

        elif choice == 4:
            qty = get_units("Canadian")
            val = rCAD * qty
            print(str(qty) + " Canadian = %s " % locale.currency(val, grouping=True))
            total_currency_units[choice - 1] += qty
            total_currency_value[choice - 1] += val

        elif choice == 5:
            qty = get_units("Rubbles")
            val = rRUB * qty
            print(str(qty) + " Rubbles = %s " % locale.currency(val, grouping=True))
            total_currency_units[choice - 1] += qty
            total_currency_value[choice - 1] += val

        elif choice == 9:
            get_rates()
        else:
            print("Unknown Operation!")
        grand_total += val
        choice = get_choice()
    for i in range(0, 5):
        print(
            currency_abbreviations[i]
            + ": "
            + str(total_currency_units[i])
            + " units for a value of: %s "
            % locale.currency(total_currency_value[i], grouping=True)
        )

    print(
        "Total of all currency purchased was %s"
        % locale.currency(grand_total, grouping=True)
    )


def get_units(prompt):
    unit = -1
    while unit <= 0: 
        try:
            unit = int(input("How many " + prompt + " are you buying? "))
            if unit < 0:
                print("Unit must be greater than 0")
                unit = -1
        except ValueError:
            print("Unit must be a numeric value")
    return unit


def main():
    result = locale.setlocale(locale.LC_ALL, "")
    if result == "C" or result.startswith("C/"):
        locale.setlocale(locale.LC_ALL, "en_US")
    print("Welcome to the Foriegn Currency Calculator")
    get_rates()
    do_valuation()
    print("Thanks for using the Foriegn Currency Calculator")


if __name__ == "__main__":
    main()
