class Bank:
    """Bank"""

    def __init__(self, pennies=0, nickles=0, dimes=0, quarters=0):
        self.set_pennies(pennies)
        self.set_nickles(nickles)
        self.set_dimes(dimes)
        self.set_quarters(quarters)
        if self.is_valid():
            self.get_total()

    def set_pennies(self, pennies):
        self._pennies = pennies

    def get_pennies(self):
        return self._pennies

    def set_nickles(self, nickles):
        self._nickles = nickles

    def get_nickles(self):
        return self._nickles

    def set_dimes(self, dimes):
        self._dimes = dimes

    def get_dimes(self):
        return self._dimes

    def set_quarters(self, quarters):
        self._quarters = quarters

    def get_quarters(self):
        return self._quarters

    def is_valid(self):
        self._error_message = ""
        valid = True
        if (
            self._pennies < 0
            or self._nickles < 0
            or self._dimes < 0
            or self._quarters < 0
        ):
            self._error_message = "Coin Count cannot be negative!"
            valid = False
        return valid

    def get_error_message(self):
        return self._error_message

    def get_total(self):
        return (
            self._pennies * 0.01
            + self._nickles * 0.05
            + self._dimes * 0.1
            + self._quarters * 0.25
        )
