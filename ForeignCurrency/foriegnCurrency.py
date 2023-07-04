#! /usr/bin/env python3
# ForeignCurrency By Zach Karr

import locale

rEUR = rGBP = rJPY = 0.0


def get_rates():
    global rEUR, rGBP, rJPY
    rEUR = get_one_rate("EUR")
    rGBP = get_one_rate("GBP")
    rJPY = get_one_rate("JPY")


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
    # write a choice method That
    # returns only 0 - 3 or 9
    choice = int(input("Currency? 1=EUR, 2=GBP, 3=JPY, 9=New Rates, 0=Quit: "))
    return choice


def do_valuation():
    global rEUR, rGBP, rJPY
    # fix grand total
    grand_total = 0.0
    choice = get_choice()
    while choice != 0:
        print("Your choice was: " + str(choice))
        if choice == 1:
            qty = get_units("Euros")
            val = rEUR * qty
            print(str(qty) + " Euros = %s " % locale.currency(val, grouping=True))
        elif choice == 9:
            get_rates()
        else:
            print("Unknown Operation!")
        grand_total += val
        choice = get_choice()
    print(
        "Total of all currency purchased was %s"
        % locale.currency(grand_total, grouping=True)
    )


def get_units(prompt):
    # must return a non-negative int
    unit = int(input("How many " + prompt + " are you buying? "))
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
