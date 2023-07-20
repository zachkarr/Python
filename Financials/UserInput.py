#Financials by Zach Karr

class UserInput:
    @staticmethod
    def getInt(prompt, floor=None, ceiling=None):
        good_value = False
        while not good_value:
            try:
                value = int(input(prompt))
                good_value = True
                if floor != None and value < floor:
                    print(
                        "Your value of "
                        + str(value)
                        + " was below the floor of: "
                        + str(floor)
                    )
                    good_value = False
                if ceiling != None and value > ceiling:
                    print(
                        "Your value of "
                        + str(value)
                        + " was above the ceiling of: "
                        + str(ceiling)
                    )
                    good_value = False
            except ValueError:
                print("Illegal input: not an integer")
                good_value = False
        return value

    def getFloat(prompt, floor=None, ceiling=None):
        good_value = False
        while not good_value:
            try:
                value = float(input(prompt))
                good_value = True
                if floor != None and value < floor:
                    print(
                        "Your value of "
                        + str(value)
                        + " was below the floor of: "
                        + str(floor)
                    )
                    good_value = False
                if ceiling != None and value > ceiling:
                    print(
                        "Your value of "
                        + str(value)
                        + " was above the ceiling of: "
                        + str(ceiling)
                    )
                    good_value = False
            except ValueError:
                print("Illegal input: not a float")
                good_value = False
        return value
