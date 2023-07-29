#! /usr/bin/env python3
# Depreciation by Zach Karr

import locale
import os
from UserInput import UserInput
from AssetSL import AssetSL
from AssetDDL import AssetDDL

cost = 0.0
salvage = 0.0
life = 0


def main():
    global cost, salvage, life
    result = locale.setlocale(locale.LC_ALL, "")
    if result == "C" or result.startswith("C/"):
        locale.setlocale(locale.LC_ALL, "en_US")
    choice = input("Asset by <i>nput, <f>ile, or <q>uit: ")
    while len(choice) > 0 and choice[0].lower() != "q":
        if choice[0].lower() == "i":
            cost = UserInput.getFloat("Asset Cost: ")
            salvage = UserInput.getFloat("Salvage Value: ")
            life = UserInput.getInt("Life (in years): ")
        elif choice[0].lower() == "f":
            path = get_asset_file()
        else:
            print("Unknown operation.")
        if cost > 0:
            do_depreciation()
        else:
            print("Asset values not processed")

        choice = input("Asset by <i>nput, <f>ile, or <q>uit: ")
    print("Thanks for using the Depreciation calculator!")


def get_asset_file():
    global cost, salvage, life
    assets = []
    file_number = 0
    print("Asset Files Available: ")
    current_working_directory = os.getcwd()
    for entry in os.listdir(current_working_directory):
        path = os.path.join(current_working_directory, entry)
        if os.path.isfile(path) and entry.endswith(".ast"):
            file_number += 1
            print(str(file_number) + ": " + entry)
            assets.append(path)
    try:
        if file_number == 0:
            cost = 0.0
            salvage = 0.0
            life = 0
            return None
        if file_number == 1:
            path = assets[0]
        else:
            path = ""
            while path == "":
                file_number = int(input("\nWhich Asset File (#): "))
                if file_number < 1 or file_number > len(assets):
                    print("File number is out of range")
                else:
                    path = assets[file_number - 1]
    except ValueError:
        print("Invalid file number")
    try:
        file = open(path, "r")
        cost = float(file.readline())
        salvage = float(file.readline())
        life = int(file.readline())
        file.close()
        return path
    except OSError as ex:
        print("Asset File not read: " + str(ex))
        cost = 0.0
        salvage = 0.0
        life = 0
    except ValueError as ex:
        print("Asset File is invalid: " + str(ex))
        cost = 0.0
        salvage = 0.0
        life = 0
    return None


def do_depreciation():
    global cost, salvage, life
    asl = AssetSL(cost, salvage, life)
    ddl = AssetDDL(cost, salvage, life)
    if asl.is_valid():
        # display result values
        print(
            "Asset has Straight Line Annual Depreciation of %s "
            % locale.currency(asl.get_annual_depreciation(), grouping=True)
        )
        print(
            "The first year depreciation for DLL would be %s "
            % locale.currency(ddl.get_first_year_depreciation(), grouping=True)
        )
        schedule = input(
            "Schedule? <S>traight Line, <D>ouble Declining, <A>ll, <N>one: "
        )
        if len(schedule) > 0 and schedule[0].upper() == "S":
            print("     Straight Line Depreciation Schedule")
            print(" Year    Beg.Bal       Ann.Dep      End.Bal")
            for i in range(1, asl.get_life() + 1):
                print(
                    "{:4}".format(i)
                    + "{:13,.2f} {:13,.2f} {:13,.2f}".format(
                        asl.get_beginning_balance(i),
                        asl.get_annual_depreciation(),
                        asl.get_ending_balance(i),
                    )
                )
        elif len(schedule) > 0 and schedule[0].upper() == "D":
            print("     Double Declining Depreciation Schedule")
            print(" Year    Beg.Bal       Ann.Dep      End.Bal")
            for i in range(1, ddl.get_life() + 1):
                print(
                    "{:4}".format(i)
                    + "{:13,.2f} {:13,.2f} {:13,.2f}".format(
                        ddl.get_beginning_balance(i),
                        ddl.get_annual_depreciation(i),
                        ddl.get_ending_balance(i),
                    )
                )
        elif len(schedule) > 0 and schedule[0].upper() == "A":
            print("     Straight Line Depreciation Schedule")
            print(" Year    Beg.Bal       Ann.Dep      End.Bal")
            for i in range(1, asl.get_life() + 1):
                print(
                    "{:4}".format(i)
                    + "{:13,.2f} {:13,.2f} {:13,.2f}".format(
                        asl.get_beginning_balance(i),
                        asl.get_annual_depreciation(),
                        asl.get_ending_balance(i),
                    )
                )
            print("\n     Double Declining Depreciation Schedule")
            print(" Year    Beg.Bal       Ann.Dep      End.Bal")
            for i in range(1, ddl.get_life() + 1):
                print(
                    "{:4}".format(i)
                    + "{:13,.2f} {:13,.2f} {:13,.2f}".format(
                        ddl.get_beginning_balance(i),
                        ddl.get_annual_depreciation(i),
                        ddl.get_ending_balance(i),
                    )
                )

        else:
            print("Unknown Depreciation Schedule option")

    else:
        print("Asset error: " + asl.get_error_message())


if __name__ == "__main__":
    main()
