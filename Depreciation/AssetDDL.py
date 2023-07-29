class AssetDDL:
    """Double Declining  Depreciation"""

    def __init__(self, cost=0.0, salvage=0.0, life=0):
        self.set_cost(cost)
        self.set_salvage(salvage)
        self.set_life(life)
        if self.is_valid():
            self.build_asset()

    def set_cost(self, cost):
        self._cost = cost

    def get_cost(self):
        return self._cost

    def set_salvage(self, salvage):
        self._salvage = salvage

    def get_salvage(self):
        return self._salvage

    def set_life(self, life):
        self._life = life

    def get_life(self):
        return self._life

    def is_valid(self):
        self._error_message = ""
        valid = True
        if self._cost <= 0:
            self._error_message = "Cost must be > 0.\n"
            valid = False
        if self._salvage < 0:
            self._error_message += "Salvage cannot be negative.\n"
            valid = False
        if self._salvage >= self._cost:
            self._error_message += "Salvage cannot be >= cost.\n"
        if self._life <= 0:
            self._error_message += "Life must be > 0. \n"
            valid = False
        return valid

    def get_error_message(self):
        return self._error_message

    def build_asset(self):
        self._beginning_balance = [0.0] * self._life
        self._ending_balance = [0.0] * self._life
        self._beginning_balance[0] = self._cost
        self._annual_depreciation = [0] * self._life
        self._annual_depreciation[0] = (self._cost * 2) / self._life
        for i in range(0, self._life):
            if i > 0:
                self._beginning_balance[i] = self._ending_balance[i - 1]
                self._annual_depreciation[i] = (
                    self._beginning_balance[i] * 2
                ) / self._life

            self._ending_balance[i] = (
                self._beginning_balance[i] - self._annual_depreciation[i]
            )
            if self._annual_depreciation[i] < self._salvage:
                self._annual_depreciation[i] = self._salvage
                self._ending_balance[i] = (
                    self._beginning_balance[i] - self._annual_depreciation[i]
                )
            if (
                self._beginning_balance[i] - self._ending_balance[i] < self._salvage
                and self._ending_balance[i] > self._salvage
            ):
                self._annual_depreciation[i] = (
                    self._beginning_balance[i] - self._ending_balance[i]
                )
            if (
                self._annual_depreciation[i] == self._salvage
                and self._ending_balance[i] < self._salvage
            ):
                self._ending_balance[i] = self._salvage

                self._annual_depreciation[i] = (
                    self._beginning_balance[i] - self._ending_balance[i]
                )

            if self._beginning_balance[i] == self._salvage:
                self._annual_depreciation[i] = 0

    def get_annual_depreciation(self, year):
        if year < 1 or year > self._life:
            return -1
        return self._annual_depreciation[year - 1]

    def get_beginning_balance(self, year):
        if year < 1 or year > self._life:
            return -1
        return self._beginning_balance[year - 1]

    def get_ending_balance(self, year):
        if year < 1 or year > self._life:
            return -1
        return self._ending_balance[year - 1]

    def get_first_year_depreciation(self):
        return self._annual_depreciation[0]
