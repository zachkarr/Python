#! /usr/bin/env python3

import Converter


def main():
    print("English/Metrics Conversions")
    do_kelvin = False
    option = -1
    while option == -1:
        answer = input("On temperature conversions do you want degrees Kelvin? (Y/n): ")
        if (
            answer.startswith("Y").upper()
            and len(answer) > 0
            and answer[0].upper() == "Y"
        ):
            do_kelvin = True
        else:
            print("Illegal input try again ")
            option = -1

        choice = get_choice()
    while choice != 0:
        try:
            if choice == 1:
                # miles to Km
                miles = input("Miles? ")
                kilometers = Converter.miles_to_kilometers(miles)
                print(str(miles) + " Miles = " + str(kilometers) + " Kilometers")
            elif choice == 2:
                oz = input("Oz? ")
                grams = Converter.oz_to_grams(oz)
                print(str(oz) + " Oz = " + str(grams) + " grams")
            elif choice == 3:
                f = input("F? ")
                celcius = Converter.f_to_celcius(f)
                print(str(f) + " F = " + str(celcius) + " celcius")
            elif choice == 4:
                celcius = input("Celcius temp? ")
                # dont show illegal f temp if below absolute zero
                # f = Converter.CtoF(c)
                # print("resulting f temp")
                if do_kelvin:
                    kelvin = Converter.degrees_kelvin(celcius)
                    print("which is also a temp of " + str(round(kelvin, 3)))
            elif choice == 5:
                meters = input("Meters? ")
                feet = Converter.meters_to_feet(meters)
                print(str(meters) + " meters = " + str(feet) + " feet")

            elif choice == 6:
                liters = input("Liters? ")
                gallons = Converter.liters_to_gallons(liters)
                print(str(liters) + " liters = " + str(gallons) + " gallons")
            else:
                print("I do not have that conversion.")
        except ValueError as e:
            print("Value Error: " + str(e))
        except Exception as e:
            print("General Error: " + str(e))
        choice = get_choice()


def get_choice():
    choice = int(
        input(
            "Conversion? 1-Mi-to-Km, 2=Oz-to-Gr, 3=F-to-C, 4=C-to-F, 5=M-to-Ft, 6=Li-to-Ga, 0=quit: "
        )
    )

    return choice


if __name__ == "__main__":
    main()
