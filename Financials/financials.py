#! /usr/bin/env python3
# Financials by Zach Karr
import locale
from UserInput import UserInput
from Annuity import Annuity
from Loan import Loan


def main():
    result = locale.setlocale(locale.LC_ALL, "")
    if result == "C" or result.startswith("C/"):
        locale.setlocale(locale.LC_ALL, "en_US")
    print("Welcome to the Financials Calculator")
    choice = UserInput.getInt("Operation? 1=Annuity, 2=Loan, 0=Quit: ", 0, 2)
    while choice != 0:
        if choice == 1:
            do_annuity()
        elif choice == 2:
            do_loan()
        else:
            print("Unknown Financial Operation")
        choice = UserInput.getInt("Operation? 1=Annuity, 2=Loan, 0=Quit: ", 0, 2)

    print("Thanks for using the Financials Calculator")


def do_annuity():
    deposit = UserInput.getFloat("Monthly Deposit: ", 0)
    rate = UserInput.getFloat("Annual Interest Rate (6.25% = 6.25): ", 0)
    term = UserInput.getInt("Term (in months): ", 0)
    annuity = Annuity(deposit, rate, term)
    if annuity.is_valid():
        print(
            "A monthly deposit of %s "
            % locale.currency(annuity.get_deposit(), grouping=True)
            + " earning "
            + "{:.2%}".format(annuity.get_rate() / 100.0, grouping=True)
            + " annually after "
            + str(annuity.get_term())
            + " months will have a final value of %s "
            % locale.currency(annuity.get_final_value_of_annuity(), grouping=True)
        )
        print(
            "This includes interest earned of %s "
            % locale.currency(annuity.get_total_interested_earned(), grouping=True)
        )
        schedule = input("Full Schedule? (Y/N): ")
        if len(schedule) > 0 and schedule[0].upper() == "Y":
            # schedule was requested
            print("Month    Beg Bal       Deposit     Int Earned   End Bal")
            for i in range(1, annuity.get_term() + 1):
                print(
                    "{:4}".format(i)
                    + "{:12,.2f} {:12,.2f} {:12,.2f} {:12,.2f}".format(
                        annuity.get_beginning_balance(i),
                        annuity.get_deposit(),
                        annuity.get_interest_earned(i),
                        annuity.get_ending_balance(i),
                    )
                )
    else:
        print("Validation errors: " + annuity.get_error_message())


def do_loan():
    amount = UserInput.getFloat("Loan Amount: ", 0)
    rate = UserInput.getFloat("Annual Interest Rate (6.25% = 6.25): ", 0)
    term = UserInput.getInt("Term (in months): ", 0)
    loan = Loan(amount, rate, term)
    if loan.is_valid():
        print(
            "A Loan of %s " % locale.currency(loan.get_amount(), grouping=True)
            + "charging "
            + "{:.2%}".format(loan.get_rate() / 100.0, grouping=True)
            + " annually with a term of "
            + str(loan.get_term())
            + " months will require a monthly payment of: %s "
            % locale.currency(loan.get_monthly_payment(), grouping=True)
        )
        print(
            "That includes an interest charge of "
            + locale.currency(loan.get_interest(), grouping=True)
        )
        schedule = input("Full Schedule? (Y/N): ")
        if len(schedule) > 0 and schedule[0].upper() == "Y":
            print("Month       Beg Bal     Pmt     Int Charged     End Bal ")
            for i in range(1, loan.get_term() + 1):
                print(
                    "{:4}".format(i)
                    + "{:12,.2f} {:12,.2f} {:12,.2f} {:12,.2f}".format(
                        loan.get_beginning_balance(i),
                        loan.get_monthly_payment(),
                        loan.get_interest_charged(i),
                        loan.get_ending_balance(i),
                    )
                )


if __name__ == "__main__":
    main()
