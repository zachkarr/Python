# Annuity class - Calculates future value of annuity


class Annuity:
    """Annuity Calculator"""

    def __init__(self, deposit=0.0, rate=0.0, term=0):
        self.set_deposit(deposit)
        self.set_rate(rate)
        self.set_term(term)
        self.validate()
        # build all values needed if start values are valid
        if self._isvalid:
            self.build_annuity()

    def set_deposit(self, deposit):
        # internal variables using self are pseudo private
        self._deposit = deposit

    def get_deposit(self):
        return self._deposit

    def set_rate(self, rate):
        self._rate = rate

    def get_rate(self):
        return self._rate

    def set_term(self, term):
        self._term = term

    def get_term(self):
        return self._term

    def validate(self):
        self._error = ""
        self._isvalid = True
        if self._deposit <= 0:
            self._error = "Annuity deposit must be greater than 0 \n"
            self._isvalid = False
        # validate rate as between 0 and 25
        if self._rate < 1 or self._rate > 25:
            self._error += (
                "Rate appears to be out of bounds (must be between 1 and 25) \n"
            )
            self._isvalid = False
        if self._term <= 0:
            self._error += "Term must be > 0 \n"
            self._isvalid = False

    def is_valid(self):
        return self._isvalid

    def get_error_message(self):
        return self._error

    def build_annuity(self):
        # build will calculate all schedule values
        # and put into separate lists: beginning_balance, interest_earned, ending_balance
        self._beginning_balance = [0] * self._term  # creates a list of term zero values
        self._interest_earned = [0] * self._term
        self._ending_balance = [0] * self._term

        monthly_rate = self._rate / 12.0 / 100
        self._beginning_balance[0] = 0  # reinforces idea that annuity starts at zero
        for i in range(0, self._term):
            if i > 0:
                self._beginning_balance[i] = self._ending_balance[i - 1]
            self._interest_earned[i] = (
                self._beginning_balance[i] + self._deposit
            ) * monthly_rate
            self._ending_balance[i] = (
                self._beginning_balance[i] + self._deposit + self._interest_earned[i]
            )

    def get_final_value_of_annuity(self):
        return self._ending_balance[self._term - 1]

    def get_beginning_balance(self, month):
        # assumes that month is 1 to term (not 0 to term)
        if month < 1 or month > self._term:
            return -1
        return self._beginning_balance[month - 1]

    def get_interest_earned(self, month):
        if month < 1 or month > self._term:
            return -1
        return self._interest_earned[month - 1]

    def get_ending_balance(self, month):
        if month < 1 or month > self._term:
            return -1
        return self._ending_balance[month - 1]

    def get_total_interested_earned(self):
        return self._ending_balance[self._term - 1] - (self._deposit * self._term)
