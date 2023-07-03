#! /usr/bin/env python3
# TimeValueOfMoney by Zach Karr

import locale


def main():
    result = locale.setlocale(locale.LC_ALL, "")
    if result == "C" or result.startswith("C/"):
        locale.setlocale(locale.LC_ALL, "en_US")

    choice = get_choice()
    while choice != 0:
        if choice == 1:
            future_value = get_value("Future Value: ")
            rate = get_value("Annual Interest Rate (6.25% = 6.25): ")
            term = get_value("Term (in months): ")
            try:
                present_value = calculate_present_value(future_value, rate, term)
                print(
                    "An amount of %s " % locale.currency(future_value, grouping=True)
                    + "to be received in "
                    + str(term)
                    + " months "
                    + "with an annual interest rate of %s%% " % rate
                    + "has a value today of: %s "
                    % locale.currency(present_value, grouping=True)
                    + "that includes a discount of %s "
                    % locale.currency(future_value - present_value, grouping=True)
                )
            except UnboundLocalError:
                print(
                    "Could not correctly calculate based on wrong/missing input values. Try again? "
                )
        elif choice == 2:
            deposit = get_value("Initial Deposit: ")
            rate = get_value("Annual Interest Rate (6.25% = 6.25): ")
            term = get_value("Term (in months): ")
            try:
                future_value = calculate_future_value(deposit, rate, term)
                print(
                    "A deposit of %s " % locale.currency(deposit, grouping=True)
                    + "earning %s%%" % rate
                    + " for "
                    + str(term)
                    + " months will have a future value of %s "
                    % locale.currency(future_value, grouping=True)
                )
            except UnboundLocalError:
                print(
                    "Could not correctly calculate based on wrong/missing input values. Try again? "
                )

        elif choice == 3:
            deposit = get_value("Monthly Deposits: ")
            rate = get_value("Annual Interest Rate (6.25% = 6.25): ")
            term = get_value("Term (in months): ")
            try:
                future_value_of_annuity = calculate_future_value_of_annuity(
                    deposit, rate, term
                )
                print(
                    "A monthly deposit of %s " % locale.currency(deposit, grouping=True)
                    + "earning %s%% " % rate
                    + "annually after "
                    + str(term)
                    + " months will have a final value of %s "
                    % locale.currency(future_value_of_annuity, grouping=True)
                )
            except UnboundLocalError:
                print(
                    "Could not correctly calculate based on wrong/missing input values. Try again? "
                )
        else:
            print("Unknown operation " + str(choice))
        choice = get_choice()
    print("Thanks for using the Time Value of Money program!")


def calculate_present_value(future_value, rate, term):
    try:
        monthly_rate = rate / 100 / 12
        present_value = future_value / pow(1 + monthly_rate, term)
    except TypeError:
        print(
            "Wrong data types(s) were entered and we cannot correctly calculate the present value, sorry!"
        )
    except UnboundLocalError:
        print("Present Value must be associated with a value")
    return present_value


def calculate_future_value(deposit, rate, term):
    try:
        monthly_rate = rate / 100 / 12
        future_value = deposit * pow(1 + monthly_rate, term)
    except TypeError:
        print(
            "Wrong data types(s) were entered and we cannot correctly calculate the future value, sorry!"
        )
    except UnboundLocalError:
        print("Future Value must be associated with a value")
    return future_value


def calculate_future_value_of_annuity(deposit, rate, term):
    try:
        monthly_rate = rate / 100 / 12
        future_value_of_annuity = 0.0
        for i in range(0, term):
            interest_earned = (future_value_of_annuity + deposit) * monthly_rate
            future_value_of_annuity += deposit + interest_earned
    except TypeError:
        print(
            "Wrong data type(s) were entered and we cannot correcly calculate the value of the annuity, sorry!"
        )
    except UnboundLocalError:
        print("Future Value of Annuity must be associated with a value")
    return future_value_of_annuity


def get_value(prompt):
    control = False
    while control == False:
        try:
            value = float(input(prompt))
            control = True
            if value % 1 == 0:
                value = int(value)
                control = True
            if value < 0 and prompt == "Term (in months): ":
                print("Value must be greater than 0")
                control = False
        except ValueError:
            print("Wrong input value, try again")
            control = False
    return value


def get_choice():
    choice = -1
    while choice < 0 or choice > 3:
        try:
            choice = int(input("Operation? 1 = PV, 2 = FV, 3 = FV-Annuity, 0 = Quit: "))
            if choice < 0 or choice > 3:
                print("Operation unknown: must be 0-3 ")
        except ValueError:
            print("Illegal input: not an integer between 0-3 ")
            choice = -1
    return choice


if __name__ == "__main__":
    main()
